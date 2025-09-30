import argparse
import os
import platform
import signal
import subprocess
import sys

from dotenv import load_dotenv

from .util import find_webots_install_path

"""
Usage: webots-controller [options] [controller_file] [controller_args]

Options:

  --help
    Display this help message and exit.

  --protocol=<ipc|tcp>
    Define the protocol to use to communicate between the controller and Webots.
    'ipc' is used by default. 'ipc' should be used when Webots is
    running on the same machine as the extern controller.
    'tcp' should be used when connecting to a remote instance of Webots.

  --ip-address=<ip-address>
    The IP address of the remote machine on which the Webots instance is running.
    This option should only be used with the `tcp` protocol
    (i.e. remote controllers).

  --port=<port>
    Define the port to which the controller should connect.
    1234 is used by default, as it is the default port for Webots.
    This setting allows you to connect to a specific instance of Webots if
    there are multiple instances running on the target machine.
    The port of a Webots instance can be set at its launch.

  --robot-name=<robot-name>
    Target a specific robot by specifying its name in case multiple robots wait
    for an extern controller in the Webots instance.

  --interactive
    Launch MATLAB in interactive debugging mode.
    See https://cyberbotics.com/doc/guide/matlab#using-the-matlab-desktop for
    more information.

  --matlab-path=<matlab-path>
    For MATLAB controllers, this option allows to specify the path to the
    executable of a specific MATLAB version.
    By default, the launcher checks in the default MATLAB installation folder.
    See https://cyberbotics.com/doc/guide/running-extern-robot-controllers#running-a-matlab-extern-controller
    for more information.

  --stdout-redirect
    Redirect the stdout of the controller to the Webots console.

  --stderr-redirect
    Redirect the stderr of the controller to the Webots console.
"""


def default_webots_install_path():
    if platform.system() == "Windows":
        return os.path.join("C:", "Program Files", "Webots")
    elif platform.system() == "Darwin":
        return os.path.join("/Applications", "Webots.app")
    else:
        # usually linux
        return "/usr/local/webots"


def webots_controller_path(webots_home: str) -> str:
    if platform.system() == "Windows":
        return os.path.join(webots_home, "msys64", "mingw64", "bin", "webots-controller.exe")
    elif platform.system() == "Darwin":
        return os.path.join(webots_home, "Contents", "MacOS", "webots-controller")
    else:
        # ususally linux
        return os.path.join(webots_home, "webots-controller")


def verify_webots_controller_existed(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"webots-controller not found at {path}. Please set WEBOTS_HOME environment "
            "variable to your Webots installation path."
        )
    return True


def main():
    def signal_handler(signum, frame):
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    load_dotenv()  # take environment variables from .env.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--protocol", type=str, choices=["ipc", "tcp"], default="ipc", help="protocol to use"
    )
    parser.add_argument(
        "--ip-address", type=str, default="127.0.0.1", help="IP address of the Webots instance"
    )
    parser.add_argument("--port", type=int, default=1234, help="port of the Webots instance")
    parser.add_argument(
        "--robot-name", type=str, default="robot", help="name of the robot in Webots"
    )
    parser.add_argument(
        "--stdout-redirect", action="store_true", help="redirect stdout to Webots console"
    )
    parser.add_argument(
        "--stderr-redirect", action="store_true", help="redirect stderr to Webots console"
    )
    args, unknown = parser.parse_known_args()

    # Resolve WEBOTS_HOME with precedence:
    # 1. Explicit environment variable
    # 2. Auto-detected install (registry / PATH / bundle)
    # 3. Static default fallback
    detected_home = find_webots_install_path()
    if "WEBOTS_HOME" in os.environ:
        webots_home = os.environ["WEBOTS_HOME"]
    elif detected_home:
        webots_home = detected_home
    else:
        webots_home = default_webots_install_path()
    # Uncomment for troubleshooting:
    # print(f"[DEBUG] Using WEBOTS_HOME={webots_home} (detected={detected_home})")
    webots_controller = webots_controller_path(webots_home)
    verify_webots_controller_existed(webots_controller)

    cmd = [
        webots_controller,
        f"--protocol={args.protocol}",
        f"--ip-address={args.ip_address}",
        f"--port={args.port}",
        f"--robot-name={args.robot_name}",
        "--stdout-redirect" if args.stdout_redirect else "",
        "--stderr-redirect" if args.stderr_redirect else "",
        os.path.join(os.path.dirname(__file__), "server.py"),
    ] + unknown
    cmd = [c for c in cmd if c]  # remove empty string
    # print("[DEBUG] Running command:\n", " ".join(cmd))
    # Ensure WEBOTS_HOME is set for the subprocess even if it wasn't originally
    # present in the parent environment (or if we resolved a default).
    env = os.environ.copy()
    env["WEBOTS_HOME"] = webots_home
    subprocess.run(cmd, env=env)


if __name__ == "__main__":
    main()
