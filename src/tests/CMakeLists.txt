# CMake configuration for unit tests
cmake_minimum_required(VERSION 3.14)

# Add Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Add the test source file
set(TEST_SOURCES
    test_webots_grpc_client.cpp
)

# Create the test executable
add_executable(test_webots_grpc_client ${TEST_SOURCES})

# Link the test executable with the necessary libraries
target_link_libraries(test_webots_grpc_client
    PRIVATE
    GTest::gtest_main
    GTest::gmock_main
    webots-grpc-client
)

# Add the test to CTest
# add_test(NAME WebotsGrpcClientTests COMMAND test_webots_grpc_client)