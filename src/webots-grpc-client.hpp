#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define WEBOTS_GRPC_EXPORT __declspec(dllexport)
#else
  #define WEBOTS_GRPC_EXPORT
#endif

WEBOTS_GRPC_EXPORT void webots_grpc();
WEBOTS_GRPC_EXPORT void webots_grpc_print_vector(const std::vector<std::string> &strings);
