import grpc
import generated.robot_pb2 as robot_pb2
import generated.robot_pb2_grpc as robot_pb2_grpc
import generated.motor_pb2 as motor_pb2
import generated.motor_pb2_grpc as motor_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel("localhost:50051")

# RobotService client
robot_stub = robot_pb2_grpc.RobotServiceStub(channel)
robot_name_response = robot_stub.GetRobotName(robot_pb2.Empty())
print("Robot Name:", robot_name_response.name)

# MotorService client
motor_stub = motor_pb2_grpc.MotorServiceStub(channel)
motor_position_response = motor_stub.GetPosition(motor_pb2.GetPositionRequest(motor_name="motor_1"))
print("Motor Position:", motor_position_response.position)