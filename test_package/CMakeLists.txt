cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(webots-grpc CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example PRIVATE webots-grpc::webots-grpc)
