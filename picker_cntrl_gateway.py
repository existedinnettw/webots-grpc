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
import paho.mqtt.client as mqtt

# import paho.mqtt.publish as publish
from typing import List, Dict

# import queue
import threading

import math
from controller import Supervisor, Motor, Robot
from controller.device import Device

# Initialize the Webots Supervisor.
# supervisor = Supervisor()
robot = Robot()
# timeStep = int(supervisor.getBasicTimeStep())
timeStep = int(robot.getBasicTimeStep())

# Initialize the arm motors and encoders.
motors: List[Motor] = []

# slider_joints = robot.getDevice("base_link").getDeviceList()  # Base node has the slider joints
for name, device in robot.devices.items():
    name: str
    device: Device
    # Check if the device is a LinearMotor

    if isinstance(device, Motor):
        motors.append(device)
        motor = device

        # motor.setVelocity(math.inf)
        # motor.setAvailableTorque(math.inf)

        position_sensor = motor.getPositionSensor()
        position_sensor.enable(timeStep)

# Now, `motors` contains all the LinearMotor devices
print("Motors found:", [motor.getName() for motor in motors])

# ======================mqtt===========


# Callback when the client connects to the broker
def on_connect(client: mqtt.Client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Subscribe to multiple topics
    client.subscribe("rb/motor_1/cntrl_pos", qos=2)
    client.subscribe("rb/motor_2/cntrl_pos", qos=2)
    client.subscribe("rb/motor_3/cntrl_pos", qos=2)
    client.subscribe("rb/step", qos=2)


# Callback when a message is received from the broker
def on_message(client: mqtt.Client, userdata: Dict, msg: mqtt.MQTTMessage):
    data = msg.payload.decode()
    print(f"Message received on {msg.topic}: {data}")
    # {
    #     "rb/step": timestamp,
    #     "rb/motor_1/cntrl_pos": 2.0
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
        "rb/motor_1/cntrl_pos": 0,  # x
        "rb/motor_2/cntrl_pos": 0,  # y
        "rb/motor_3/cntrl_pos": 0,  # z
    }
)
client.connect("192.168.29.25", 1883, 60)
client.loop_start()

try:
    # Loop 1: Draw a circle on the paper sheet.
    print("Draw a circle on the paper sheet...")

    while robot.step(timeStep) != -1:
        userdata: Dict = client.user_data_get()
        ev: threading.Event = userdata["rb/step/ev"]
        ev.wait()  # wait step received
        ev.clear()

        x = userdata["rb/motor_1/cntrl_pos"]
        y = userdata["rb/motor_2/cntrl_pos"]
        z = userdata["rb/motor_3/cntrl_pos"]
        controls = [x, y, z]

        # feedback publish
        for i in range(len(controls)):
            # client.publish(
            #     "rb/motor_{}/act_pos".format(i), controls[i], qos=2
            # )  # m.getPositionSensor().getValue()
            client.publish(
                "rb/motor_{}/act_pos".format(i),
                motors[i].getPositionSensor().getValue(),
                qos=2,
            )
        client.publish("rb/ack", userdata["rb/step"], qos=2)

        # set controls
        for i in range(len(motors)):
            motors[i].setPosition(float(controls[i]))

except KeyboardInterrupt:
    print("Disconnected and exiting...")
finally:
    # Stop the loop when you are done
    client.loop_stop()
    client.disconnect()
