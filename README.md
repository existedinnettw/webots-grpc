# webots-grpc

This project is a simple gateway convert from gRPC to webots socket IPC API. It follow some rules.

* extern controller
* synchronous simulation

```mermaid
graph LR

    A[Webots] <-->|API| B[Python extern controller gRPC service gateway]
    B <-->|gRPC| D[Python gRPC client app]
    B <-->|gRPC| C[CPP gRPC client app]
```

## run

### server

Create service from proto file,

```bash
uv run python -m grpc_tools.protoc -I ./protos --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated ./protos/*.proto
```

or generate document by [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc) plugin at the same time

```bash
uv run python -m grpc_tools.protoc -I ./protos --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated --doc_out=./doc --doc_opt=html,index.html ./protos/*.proto
```

#### execution on linux

> Modify your robot name plz.

```bash
export WEBOTS_HOME=/usr/local/webots
uv run "${WEBOTS_HOME}/webots-controller" --robot-name='robot' ./webots_grpc/server.py
```

#### execution on windows

If you use MSYS2 [as state](https://cyberbotics.com/doc/guide/compiling-controllers-in-a-terminal#windows), `export WEBOTS_HOME=C:\Program Files\Webots`

> I don't find out way to integrate `WEBOTS_HOME` yet

Or using uv directly config python path,

```ini
; .env
PYTHONPATH=C:\Program Files\Webots\lib\controller\python
```

`uv run "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='robot' .\webots_grpc\server.py`

### client

There are cpp and python client API support with unittests, plz refer python test `tests/README.md` first.

#### PYTHON

```bash
uv run python -m pytest
```

#### CPP

Check cpp client test `src/tests`

```bash
conan build . --build=missing
```
