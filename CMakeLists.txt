cmake_minimum_required(VERSION 3.15)
project(webots-grpc CXX)
set(CMAKE_CXX_STANDARD 20)

if (CMAKE_SYSTEM_NAME STREQUAL "Windows")
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif ()

find_package(Protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

# proto
# https://github.com/protocolbuffers/protobuf/blob/main/docs/cmake_protobuf_generate.md
add_library(
    webots-grpc-proto
    protos/robot.proto protos/device.proto protos/motor.proto
    protos/position_sensor.proto protos/sensor.proto
    protos/distance_sensor.proto)
target_link_libraries(webots-grpc-proto PUBLIC protobuf::libprotobuf gRPC::grpc
                                               gRPC::grpc++)
# set(PROTO_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
set(PROTO_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}")
set(PROTO_IMPORT_DIRS "${CMAKE_CURRENT_LIST_DIR}/protos")
target_include_directories(webots-grpc-proto PUBLIC ${CMAKE_CURRENT_BINARY_DIR})

# following line is necessary
protobuf_generate(TARGET webots-grpc-proto IMPORT_DIRS ${PROTO_IMPORT_DIRS}
                  PROTOC_OUT_DIR "${PROTO_BINARY_DIR}")
protobuf_generate(
    TARGET
    webots-grpc-proto
    LANGUAGE
    grpc
    GENERATE_EXTENSIONS
    .grpc.pb.h
    .grpc.pb.cc
    PLUGIN
    "protoc-gen-grpc=\$<TARGET_FILE:gRPC::grpc_cpp_plugin>"
    IMPORT_DIRS
    ${PROTO_IMPORT_DIRS}
    PROTOC_OUT_DIR
    "${PROTO_BINARY_DIR}")
# Install all generated headers under PROTO_BINARY_DIR
install(
    DIRECTORY ${PROTO_BINARY_DIR}/
    DESTINATION include
    FILES_MATCHING
    PATTERN "*.pb.h")
# Install the library
install(TARGETS webots-grpc-proto)

add_subdirectory(src)
