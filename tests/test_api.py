import os
import sys

import grpc
import pytest  # noqa: F401
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
from pytest_check.check_functions import almost_equal
from pytest_check.context_manager import check

import webots_grpc.generated.device_pb2 as device_pb2
import webots_grpc.generated.distance_sensor_pb2 as distance_sensor_pb2
import webots_grpc.generated.distance_sensor_pb2_grpc as distance_sensor_pb2_grpc
import webots_grpc.generated.motor_pb2 as motor_pb2
import webots_grpc.generated.motor_pb2_grpc as motor_pb2_grpc
import webots_grpc.generated.position_sensor_pb2 as position_sensor_pb2
import webots_grpc.generated.position_sensor_pb2_grpc as position_sensor_pb2_grpc
import webots_grpc.generated.robot_pb2 as robot_pb2
import webots_grpc.generated.robot_pb2_grpc as robot_pb2_grpc
import webots_grpc.generated.sensor_pb2 as sensor_pb2
import webots_grpc.generated.sensor_pb2_grpc as sensor_pb2_grpc


@pytest.fixture(scope="module")
def grpc_channel():
    channel = grpc.insecure_channel("localhost:50051")
    yield channel
    channel.close()


@pytest.fixture(scope="module")
def robot_stub(grpc_channel):
    return robot_pb2_grpc.RobotServiceStub(grpc_channel)


@pytest.fixture(scope="module")
def motor_stub(grpc_channel):
    return motor_pb2_grpc.MotorServiceStub(grpc_channel)


@pytest.fixture(scope="module")
def position_sensor_stub(grpc_channel):
    return position_sensor_pb2_grpc.PositionSensorServiceStub(grpc_channel)


@pytest.fixture(scope="module")
def distance_sensor_stub(grpc_channel):
    return distance_sensor_pb2_grpc.DistanceSensorServiceStub(grpc_channel)


def test_reflection(grpc_channel):
    reflection_db = ProtoReflectionDescriptorDatabase(grpc_channel)
    services = reflection_db.get_services()
    print(f"found services: {services}")

    # Check if the robot service is available
    assert "webots.RobotService" in services, "Robot service not found in reflection response"


def test_get_robot_name(robot_stub):
    response = robot_stub.GetRobotName(empty_pb2.Empty())
    assert response.name  # Should not be empty
    assert response.name == "robot"


def test_get_basic_time_step(robot_stub):
    response = robot_stub.GetBasicTimeStep(empty_pb2.Empty())
    assert response.basic_time_step > 0


def test_get_device_list(robot_stub):
    response = robot_stub.GetDeviceList(empty_pb2.Empty())
    assert len(response.devices) > 0


def test_motor_api(robot_stub, motor_stub, position_sensor_stub):
    device_list = robot_stub.GetDeviceList(empty_pb2.Empty())
    motor_names = [
        d.name
        for d in device_list.devices
        if ("motor" in d.name or "_to_" in d.name) and "sensor" not in d.name
    ]
    print("Motor Names:", motor_names)
    assert motor_names

    motor_name = motor_names[0]
    assert motor_name == "linear motor"

    device_response = robot_stub.GetDevice(device_pb2.DeviceRequest(name=motor_name))
    motor_request = motor_pb2.MotorRequest(name=device_response.name)
    motor_response = motor_stub.GetMotor(motor_request)
    assert motor_response.device.name == motor_name

    max_pos = motor_stub.GetMaxPosition(motor_request).max_position
    min_pos = motor_stub.GetMinPosition(motor_request).min_position
    with check:
        almost_equal(max_pos, 0.2, rel=1e-6)
    with check:
        almost_equal(min_pos, 0, rel=1e-6)

    pos_sensor_name = motor_stub.GetPositionSensor(motor_request).position_sensor_name
    assert pos_sensor_name
    assert pos_sensor_name == "linear motor sensor"

    # Enable position sensor
    position_sensor_stub.Enable(sensor_pb2.EnableRequest(name=pos_sensor_name, sampling_period=32))

    # Get position sensor value
    value = position_sensor_stub.GetValue(
        position_sensor_pb2.PositionSensorRequest(name=pos_sensor_name)
    ).value
    assert isinstance(value, float)

    # Set random position and step simulation
    import random

    position = min_pos + (max_pos - min_pos) * random.uniform(0, 1)
    motor_stub.SetPosition(motor_pb2.SetPositionRequest(name=motor_name, position=position))

    # Step simulation
    robot_stub.Step(robot_pb2.StepRequest(time_step=500)).success

    # Get updated position sensor value
    updated_value = position_sensor_stub.GetValue(
        position_sensor_pb2.PositionSensorRequest(name=pos_sensor_name)
    ).value
    assert pytest.approx(updated_value, 0.01) == position


def test_motor_limit_api(robot_stub, motor_stub, position_sensor_stub):
    motor_name = "linear motor"

    max_pos = motor_stub.GetMaxPosition(motor_pb2.MotorRequest(name=motor_name))
    min_pos = motor_stub.GetMinPosition(motor_pb2.MotorRequest(name=motor_name))
    with check:
        almost_equal(max_pos.max_position, 0.200, rel=1e-6)
    with check:
        almost_equal(min_pos.min_position, -0.000, rel=1e-6)


def test_motor_speed_api(robot_stub, motor_stub, position_sensor_stub):
    motor_name = "linear motor"
    pos_sensor_name = "linear motor sensor"

    position_sensor_stub.Enable(sensor_pb2.EnableRequest(name=pos_sensor_name, sampling_period=32))
    motor_stub.SetPosition(motor_pb2.SetPositionRequest(name=motor_name, position=0.1))
    assert robot_stub.Step(robot_pb2.StepRequest(time_step=320)).success
    max_velocity = motor_stub.GetMaxVelocity(motor_pb2.MotorRequest(name=motor_name))
    with check:
        almost_equal(max_velocity.velocity, 10.0, rel=1e-6)  # from robot model

    """
    TODO
    Following test actually fails, motor limit not work when SetPosition to -inf,
     which is bug from webots.
    Current hotfix is to limit the position value first in motor_service.py.
    """
    motor_stub.SetPosition(motor_pb2.SetPositionRequest(name=motor_name, position=float("-inf")))
    motor_stub.SetVelocity(motor_pb2.SetVelocityRequest(name=motor_name, velocity=0.5))
    motor_velocity = motor_stub.GetVelocity(motor_pb2.MotorRequest(name=motor_name))
    with check:
        almost_equal(motor_velocity.velocity, 0.5, rel=1e-6)
    assert robot_stub.Step(robot_pb2.StepRequest(time_step=500)).success
    value = position_sensor_stub.GetValue(
        position_sensor_pb2.PositionSensorRequest(name=pos_sensor_name)
    ).value
    with check:
        almost_equal(value, 0.00, rel=0.05)  # min pos

    # https://cyberbotics.com/doc/reference/motor?tab-language=python#velocity-control
    motor_stub.SetPosition(motor_pb2.SetPositionRequest(name=motor_name, position=float("inf")))
    motor_stub.SetVelocity(motor_pb2.SetVelocityRequest(name=motor_name, velocity=0.5))
    assert robot_stub.Step(robot_pb2.StepRequest(time_step=500)).success
    value = position_sensor_stub.GetValue(
        position_sensor_pb2.PositionSensorRequest(name=pos_sensor_name)
    ).value
    with check:
        almost_equal(value, 0.201, rel=0.05)  # max pos


def test_distance_sensor_api(robot_stub, motor_stub, position_sensor_stub, distance_sensor_stub):
    motor_name = "linear motor"
    pos_sensor_name = "linear motor sensor"

    pos_ds_name = "pos ds"
    neg_ds_name = "neg ds"
    home_ds_name = "home ds"
    sample_period = 32

    position_sensor_stub.Enable(
        sensor_pb2.EnableRequest(name=pos_sensor_name, sampling_period=sample_period)
    )
    distance_sensor_stub.Enable(
        sensor_pb2.EnableRequest(name=pos_ds_name, sampling_period=sample_period)
    )
    distance_sensor_stub.Enable(
        sensor_pb2.EnableRequest(name=neg_ds_name, sampling_period=sample_period)
    )
    distance_sensor_stub.Enable(
        sensor_pb2.EnableRequest(name=home_ds_name, sampling_period=sample_period)
    )

    ans_mat = [
        [lambda x: x > 3000, lambda x: x < 1000, lambda x: x < 1000],
        [lambda x: x < 1000, lambda x: x < 1000, lambda x: x < 1000],
        [lambda x: x < 1000, lambda x: x < 1000, lambda x: x > 3000],
    ]
    for target_pos, ans in zip([0, 0.1, 0.2 - 1e-6], ans_mat):
        motor_stub.SetPosition(motor_pb2.SetPositionRequest(name=motor_name, position=target_pos))
        assert robot_stub.Step(robot_pb2.StepRequest(time_step=500)).success
        assert (
            pytest.approx(
                position_sensor_stub.GetValue(
                    position_sensor_pb2.PositionSensorRequest(name=pos_sensor_name)
                ).value,
                0.01,
            )
            == target_pos
        )

        assert ans[0](
            distance_sensor_stub.GetValue(
                distance_sensor_pb2.DistanceSensorRequest(name=neg_ds_name)
            ).value
        )
        assert ans[1](
            distance_sensor_stub.GetValue(
                distance_sensor_pb2.DistanceSensorRequest(name=home_ds_name)
            ).value
        )
        assert ans[2](
            distance_sensor_stub.GetValue(
                distance_sensor_pb2.DistanceSensorRequest(name=pos_ds_name)
            ).value
        )
