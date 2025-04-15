# webots mqtt

This project is a simple gateway convert from mqtt message to webots socket IPC API. It follow some rules.

* extern control
* synchronous simulation

### tree

If you have no robot description file, `descriptions` folder offer some basic one.

## build

```bash
poetry run python -m grpc_tools.protoc -I ./protos --python_out=./generated --grpc_python_out=./generated ./protos/*.proto
```

`grpcurl -plaintext localhost:50051 list`
`grpcurl -plaintext localhost:50051 describe device.DeviceService`

### for windows

If you use MSYS2 [as state](https://cyberbotics.com/doc/guide/compiling-controllers-in-a-terminal#windows), `export WEBOTS_HOME=C:\Program Files\Webots`

> I don't find out way to integrate `WEBOTS_HOME` yet

[extern controller](https://cyberbotics.com/doc/guide/running-extern-robot-controllers#launcher), e.g. 

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --help`

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='IRB 4600/40' xxx.py`

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='Picker' picker_cntrl_gateway.py`

`poetry run "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='Picker' .\webots_grpc\server.py`