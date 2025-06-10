#client
add_library(
    webots-grpc-client device_client.cpp motor_client.cpp robot_client.cpp
                       position_sensor_client.cpp distance_sensor_client.cpp)
target_include_directories(webots-grpc-client PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(webots-grpc-client PUBLIC webots-grpc-proto gRPC::grpc
                                                gRPC::grpc++)
set_target_properties(
    webots-grpc-client
    PROPERTIES
        PUBLIC_HEADER
        "webots-grpc-client.hpp;motor_client.hpp;device_client.hpp;robot_client.hpp;position_sensor_client.hpp;distance_sensor_client.hpp"
)
install(TARGETS webots-grpc-client)

if (NOT BUILD_TESTING STREQUAL OFF)
    enable_testing()
    add_subdirectory(tests)
endif ()
