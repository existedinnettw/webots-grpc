from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import can_run, check_min_cppstd  # noqa: F401
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class webots_grpcRecipe(ConanFile):
    name = "webots-grpc"
    version = "0.1.3"
    package_type = "library"

    # Optional metadata
    license = "MPL-2.0"
    author = "insleker <bkinnightskytw@gmail.com>"
    url = "https://github.com/existedinnettw/webots-grpc"
    description = "webots gRPC gateway and client"
    topics = ("webots", "gRPC", "client", "gateway")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}

    default_options = {
        "shared": False,
        "fPIC": True,
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "protos/*"

    def validate(self):
        check_min_cppstd(self, "20")  # grpc

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def requirements(self):
        # Fix for gRPC metric name registration issue - set secure=True
        # See: https://github.com/conan-io/conan-center-index/issues/25107
        self.requires(
            "grpc/1.67.1", options={"secure": True}, transitive_headers=True, transitive_libs=True
        )
        self.requires("protobuf/5.27.0", transitive_headers=True)  # must matched grpc

        # build
        self.tool_requires("cmake/[>=3.14 <=4]")
        # protoc compiler needs to run on host architecture during cross-compilation
        self.tool_requires("protobuf/5.27.0")
        # grpc_cpp_plugin needs to run on host architecture during cross-compilation
        self.tool_requires("grpc/1.67.1", options={"secure": True})

        # test
        self.test_requires("gtest/[~1]")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        # if (not self.conf.get("tools.build:skip_test", default=False)) and can_run(self):
        #     cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["webots-grpc-client", "webots-grpc-proto"]
