import importlib
import sys
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import webots_grpc.util as util_mod


def reload_module():
    return importlib.reload(util_mod)


def test_find_webots_install_path_windows_registry_success(monkeypatch):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Windows")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)

    class DummyKey:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    fake_winreg = SimpleNamespace(
        HKEY_LOCAL_MACHINE=object(),
        OpenKey=MagicMock(return_value=DummyKey()),
        QueryValueEx=MagicMock(return_value=(r"C:\Program Files\Webots", None)),
    )

    with patch.dict(sys.modules, {"winreg": fake_winreg}):
        reload_module()  # ensure our patched winreg is used upon import if needed
        expected = r"C:\Program Files\Webots"
        # Patch exists so registry path considered valid even if not present locally
        original_exists = util_mod.os.path.exists
        monkeypatch.setattr(
            util_mod.os.path,
            "exists",
            lambda p, _orig=original_exists: True if p == expected else _orig(p),
        )
        assert util_mod.find_webots_install_path() == expected


def test_find_webots_install_path_windows_registry_missing(monkeypatch):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Windows")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)

    class DummyKey:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def open_key_fail(*args, **kwargs):  # noqa: D401
        raise FileNotFoundError

    fake_winreg = SimpleNamespace(
        HKEY_LOCAL_MACHINE=object(),
        OpenKey=MagicMock(side_effect=open_key_fail),
        QueryValueEx=MagicMock(),
    )

    with patch.dict(sys.modules, {"winreg": fake_winreg}):
        reload_module()
        # Ensure default directory heuristics won't find a path by
        # pointing ProgramFiles to temp locations.
        monkeypatch.setenv("ProgramFiles", r"C:\NonExistingPF")
        monkeypatch.setenv("ProgramFiles(x86)", r"C:\NonExistingPFx86")
        # Monkeypatch exists to always return False for those.
        monkeypatch.setattr(
            util_mod.os.path,
            "exists",
            lambda p: False,
        )
        assert util_mod.find_webots_install_path() is None


def test_find_webots_install_path_windows_env_var_precedence(monkeypatch, tmp_path):
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Windows")
    fake_home = tmp_path / "Webots"
    fake_home.mkdir()
    monkeypatch.setenv("WEBOTS_HOME", str(fake_home))
    # Even if registry would fail, env var should take precedence.
    with patch.dict(sys.modules, {"winreg": object()}):  # dummy
        reload_module()
        assert util_mod.find_webots_install_path() == str(fake_home)


def test_find_webots_install_path_windows_wow6432node(monkeypatch):
    """Ensure WOW6432Node view also works."""
    monkeypatch.setattr(util_mod.platform, "system", lambda: "Windows")
    monkeypatch.delenv("WEBOTS_HOME", raising=False)

    class DummyKey:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    # First key (regular) raises, second (wow6432) returns value
    def open_key_side_effect(hive, subkey):  # noqa: D401
        if "WOW6432Node" in subkey:
            return DummyKey()
        raise FileNotFoundError

    fake_winreg = SimpleNamespace(
        HKEY_LOCAL_MACHINE=object(),
        OpenKey=MagicMock(side_effect=open_key_side_effect),
        QueryValueEx=MagicMock(return_value=(r"C:\Program Files (x86)\Webots", None)),
    )
    with patch.dict(sys.modules, {"winreg": fake_winreg}):
        reload_module()
        expected = r"C:\Program Files (x86)\Webots"
        original_exists = util_mod.os.path.exists
        monkeypatch.setattr(
            util_mod.os.path,
            "exists",
            lambda p, _orig=original_exists: True if p == expected else _orig(p),
        )
        assert util_mod.find_webots_install_path() == expected
