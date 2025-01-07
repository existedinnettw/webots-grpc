# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstration of inverse kinematics using the "ikpy" Python module."""

import sys
import tempfile
import paho.mqtt.client as mqtt

# import paho.mqtt.publish as publish
from typing import List, Dict

# import queue
import threading

try:
    import ikpy
    from ikpy.chain import Chain
except ImportError:
    sys.exit(
        'The "ikpy" Python module is not installed. '
        'To run this sample, please upgrade "pip" and install ikpy with this command: "pip install ikpy"'
    )

import math
from controller import Supervisor, Motor

if ikpy.__version__[0] < "3":
    sys.exit(
        'The "ikpy" Python module version is too old. '
        'Please upgrade "ikpy" Python module to version "3.0" or newer with this command: "pip install --upgrade ikpy"'
    )


IKPY_MAX_ITERATIONS = 13

# Initialize the Webots Supervisor.
supervisor = Supervisor()
timeStep = int(supervisor.getBasicTimeStep())

# Create the arm chain from the URDF
filename = None
with tempfile.NamedTemporaryFile(suffix=".urdf", delete=False) as file:
    filename = file.name
    print(filename)
    file.write(supervisor.getUrdf().encode("utf-8"))
# armChain = Chain.from_urdf_file(
#     filename, active_links_mask=[False, True, True, True, True, True, True, False]
# )
armChain = Chain.from_urdf_file(
    filename, active_links_mask=[False, True, True, True, True, True, True]
)

# Initialize the arm motors and encoders.
motors: List[Motor] = []
for link in armChain.links:
    if "motor" in link.name:
        print("name:'{}'".format(link.name))
        motor: Motor = supervisor.getDevice(link.name)
        # motor.setVelocity(2.0)

        motor.setVelocity(math.inf)
        motor.setAvailableTorque(math.inf)

        position_sensor = motor.getPositionSensor()
        position_sensor.enable(timeStep)
        motors.append(motor)

# Get the arm and target nodes.
target = supervisor.getFromDef("TARGET")
arm = supervisor.getSelf()


# ======================mqtt===========


# Callback when the client connects to the broker
def on_connect(client: mqtt.Client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Subscribe to multiple topics
    client.subscribe("rb/A_motor/cntrl_pos", qos=2)
    client.subscribe("rb/B_motor/cntrl_pos", qos=2)
    client.subscribe("rb/C_motor/cntrl_pos", qos=2)
    client.subscribe("rb/step", qos=2)


# Callback when a message is received from the broker
def on_message(client: mqtt.Client, userdata: Dict, msg: mqtt.MQTTMessage):
    data = msg.payload.decode()
    print(f"Message received on {msg.topic}: {data}")
    # {
    #     "rb/step": timestamp,
    #     "rb/A_motor/cntrl_pos": 2.0
    # }
    userdata[msg.topic] = data
    if msg.topic == "rb/step":
        ev: threading.Event = userdata["rb/step/ev"]
        ev.set()


client = mqtt.Client()
# Set the callbacks
client.on_connect = on_connect
client.on_message = on_message
client.user_data_set(
    userdata={
        "rb/step": 0,
        "rb/step/ev": threading.Event(),
        "rb/A_motor/cntrl_pos": 1.5,  # x
        "rb/B_motor/cntrl_pos": 0,  # y
        "rb/C_motor/cntrl_pos": 0.2,  # z
    }
)
client.connect("192.168.29.25", 1883, 60)
client.loop_start()

try:
    # Loop 1: Draw a circle on the paper sheet.
    print("Draw a circle on the paper sheet...")

    while supervisor.step(timeStep) != -1:
        userdata: Dict = client.user_data_get()
        ev: threading.Event = userdata["rb/step/ev"]
        ev.wait()  # wait step received
        ev.clear()
        x = userdata["rb/A_motor/cntrl_pos"]
        y = userdata["rb/B_motor/cntrl_pos"]
        z = userdata["rb/C_motor/cntrl_pos"]

        # feedback
        client.publish(
            "rb/A_motor/act_pos", x, qos=2
        )  # m.getPositionSensor().getValue()
        client.publish("rb/B_motor/act_pos", y, qos=2)
        client.publish("rb/C_motor/act_pos", z, qos=2)

        # wait until all control msg reached

        # Call "ikpy" to compute the inverse kinematics of the arm.
        # initial_position = [0] + [m.getPositionSensor().getValue() for m in motors] + [0]
        initial_position = [0] + [m.getPositionSensor().getValue() for m in motors]
        ikResults = armChain.inverse_kinematics(
            target_position=[x, y, z],
            target_orientation=[0, 0, -1],
            orientation_mode="X",
            max_iter=IKPY_MAX_ITERATIONS,
            initial_position=initial_position,
        )
        for i in range(6):
            motors[i].setPosition(ikResults[i + 1])

        # ================================================================================================

        # t = supervisor.getTime()

        # # Use the circle equation relatively to the arm base as an input of the IK algorithm.
        # x = 0.25 * math.cos(t) + 1.1
        # y = 0.25 * math.sin(t) - 0.95
        # z = 0.2

        # # Call "ikpy" to compute the inverse kinematics of the arm.
        # # initial_position = [0] + [m.getPositionSensor().getValue() for m in motors] + [0]
        # initial_position = [0] + [m.getPositionSensor().getValue() for m in motors]
        # ikResults = armChain.inverse_kinematics(
        #     target_position=[x, y, z],
        #     target_orientation=[0, 0, -1],
        #     orientation_mode="X",
        #     max_iter=IKPY_MAX_ITERATIONS,
        #     initial_position=initial_position,
        # )
        # # print(ikResults)

        # # Actuate the 3 first arm motors with the IK results.
        # for i in range(6):
        #     motors[i].setPosition(ikResults[i + 1])
        # # # Keep the hand orientation down.
        # # motors[4].setPosition(-ikResults[2] - ikResults[3] + math.pi / 2)
        # # # Keep the hand orientation perpendicular.
        # # motors[5].setPosition(ikResults[1])

        # # Conditions to start/stop drawing and leave this loop.
        # if supervisor.getTime() > 2 * math.pi + 1.5:
        #     break
        # elif supervisor.getTime() > 1.5:
        #     # Note: start to draw at 1.5 second to be sure the arm is well located.
        #     # supervisor.getDevice("pen").write(True)
        #     pass

except KeyboardInterrupt:
    print("Disconnected and exiting...")
finally:
    # Stop the loop when you are done
    client.loop_stop()
    client.disconnect()
