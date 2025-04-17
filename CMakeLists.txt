cmake_minimum_required(VERSION 3.15)
project(webots-grpc CXX)
set(CMAKE_CXX_STANDARD 20)

find_package(Protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

#proto
add_library(webots-grpc-proto protos/robot.proto protos/device.proto protos/motor.proto)
target_link_libraries(webots-grpc-proto
    PUBLIC
        protobuf::libprotobuf
        gRPC::grpc
        gRPC::grpc++
)
target_include_directories(webots-grpc-proto PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin LOCATION)
protobuf_generate(
    TARGET webots-grpc-proto 
    LANGUAGE cpp     
    PROTOC_OUT_DIR ${CMAKE_CURRENT_BINARY_DIR}
    IMPORT_DIRS ${CMAKE_CURRENT_LIST_DIR}/protos
)
# message(STATUS "gRPC plugin location: ${grpc_cpp_plugin_location}")
protobuf_generate(
    TARGET webots-grpc-proto 
    LANGUAGE grpc 
    GENERATE_EXTENSIONS .grpc.pb.h .grpc.pb.cc
    PLUGIN "protoc-gen-grpc=${grpc_cpp_plugin_location}"
    IMPORT_DIRS ${CMAKE_CURRENT_LIST_DIR}/protos
)

add_subdirectory(src)