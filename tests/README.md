
To run test, you need to open `tests\worlds\linear_motor.wbt` world first, then start the server(gateway) with the following command:

```bash
uv run "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='robot' .\webots_grpc\server.py
```

After that, you can run uinttest as usual:

python version tests is created by `pytest` and CPP version tests can run with `ctest`.
