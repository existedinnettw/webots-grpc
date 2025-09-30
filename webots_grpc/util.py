"""Utility helpers for Webots gRPC gateway."""

from __future__ import annotations

import os
import platform
import shutil


def find_webots_install_path() -> str | None:
    """Locate an existing Webots installation directory.

    Windows strategy (in order):
    1. Respect WEBOTS_HOME environment variable if it points to an existing path.
    2. Query uninstall registry keys (both 64-bit and 32-bit views) for InstallLocation:
       HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Webots
    3. Look in common default install directories (Program Files, Program Files (x86)).
    4. Fallback: derive from a discovered `webots-controller.exe` on PATH.

    macOS strategy:
    * If a `webots` or `webots-controller` binary is found inside a Webots.app bundle,
      return the bundle root (…/Webots.app).

    Linux / Other:
    * Attempt to locate `webots-controller` or `webots` via PATH and return its parent directory.

    Returns None if nothing suitable is found.
    """

    system = platform.system()

    # 1. Explicit env var (all platforms)
    env_home = os.getenv("WEBOTS_HOME")
    if env_home and os.path.exists(env_home):
        return env_home

    if system == "Windows":
        # 2. Registry (both views)
        try:  # pragma: no cover (import guarded for non-Windows)
            import winreg  # type: ignore
        except ImportError:  # pragma: no cover
            winreg = None  # type: ignore

        if winreg:
            reg_paths = [
                (
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Webots",
                ),
                # 32-bit view on 64-bit systems
                (
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Webots",
                ),
            ]
            for hive, subkey in reg_paths:
                try:
                    with winreg.OpenKey(hive, subkey) as key:  # type: ignore[attr-defined]
                        install_path, _ = winreg.QueryValueEx(key, "InstallLocation")  # type: ignore[attr-defined]
                        if install_path and os.path.exists(install_path):
                            return install_path
                except FileNotFoundError:
                    pass
                except OSError:
                    pass

        # 3. Common default directories
        program_files = os.environ.get("ProgramFiles", r"C:\\Program Files")
        program_files_x86 = os.environ.get("ProgramFiles(x86)", r"C:\\Program Files (x86)")
        candidates = [
            os.path.join(program_files, "Webots"),
            os.path.join(program_files_x86, "Webots"),
        ]
        for c in candidates:
            if os.path.exists(c):
                return c

        # 4. PATH discovery of controller exe
        exe = shutil.which("webots-controller.exe") or shutil.which("webots.exe")
        if exe:
            parent = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.dirname(exe)))
            )  # heuristic
            # Explanation: typical Windows structure:
            # <WEBOTS_HOME>\msys64\mingw64\bin\webots-controller.exe
            # So we ascend four levels to reach WEBOTS_HOME.
            if os.path.exists(parent):
                return parent
        return None

    # Non-Windows
    candidate = shutil.which("webots-controller") or shutil.which("webots")
    if not candidate:
        return None

    if system == "Darwin":
        token = "Webots.app"
        if token in candidate:
            prefix, _sep, _rest = candidate.partition(token)
            return os.path.join(prefix, token)

    return os.path.dirname(candidate)
