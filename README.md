# webots mqtt

This project is a simple gateway convert from mqtt message to webots socket IPC API. It follow some rules.

* extern control
* synchronous simulation

### tree

If you have no robot description file, `descriptions` folder offer some basic one.

### for windows

`export WEBOTS_HOME=C:\Program Files\Webots`

extern controller, e.g. 

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --help`

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='IRB 4600/40' xxx.py`

`& "C:\Program Files\Webots\msys64\mingw64\bin\webots-controller.exe" --robot-name='Picker' picker_cntrl_gateway.py`
