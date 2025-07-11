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
