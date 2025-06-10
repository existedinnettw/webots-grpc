# CMake configuration for unit tests
cmake_minimum_required(VERSION 3.14)

# Add Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
include(GoogleTest)

add_executable(test_api test_api.cpp)
target_link_libraries(test_api PRIVATE GTest::gtest_main GTest::gmock_main
                                       webots-grpc-client)
gtest_add_tests(TARGET test_api)

# Create the test executable
add_executable(test_webots_grpc_client test_webots_grpc_client.cpp)

# Link the test executable with the necessary libraries
target_link_libraries(
    test_webots_grpc_client PRIVATE GTest::gtest_main GTest::gmock_main
                                    webots-grpc-client)

# Add the test to CTest add_test(NAME WebotsGrpcClientTests COMMAND
# test_webots_grpc_client)
