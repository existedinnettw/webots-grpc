from conan import ConanFile
from conan.tools.build import can_run, check_min_cppstd  # noqa: F401
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class webots_grpcRecipe(ConanFile):
    name = "webots-grpc"
    version = "0.1"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of webots-grpc package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def validate(self):
        check_min_cppstd(self, "20")  # grpc

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def requirements(self):
        self.requires("grpc/1.67.1")

        # build
        self.tool_requires("cmake/[>=3.14 <=4]")

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
        self.cpp_info.libs = ["webots-grpc-client"]
