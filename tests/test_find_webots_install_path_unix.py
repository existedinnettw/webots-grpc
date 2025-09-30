import importlib
from unittest.mock import patch

import webots_grpc.util as util_mod


def reload_module():
    return importlib.reload(util_mod)


def test_find_webots_install_path_macos_app_bundle(monkeypatch):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Darwin")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)
    binary_path = "/Applications/Webots.app/Contents/MacOS/webots-controller"
    with patch.object(util_mod.shutil, "which", side_effect=[binary_path, None]):
        reload_module()
        assert util_mod.find_webots_install_path() == "/Applications/Webots.app"


def test_find_webots_install_path_linux_from_controller(monkeypatch):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Linux")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)
    binary_path = "/usr/local/webots/webots-controller"
    with patch.object(util_mod.shutil, "which", side_effect=[binary_path, None]):
        reload_module()
        assert util_mod.find_webots_install_path() == "/usr/local/webots"


def test_find_webots_install_path_linux_not_found(monkeypatch):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Linux")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)
    with patch.object(util_mod.shutil, "which", side_effect=[None, None]):
        reload_module()
        assert util_mod.find_webots_install_path() is None
