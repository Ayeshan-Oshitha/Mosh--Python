When we run a Python file, a new folder named `__pycache__` is created. This folder contains the compiled version of the modules we import, such as the `sales` module.

These compiled files are in the form of _Python bytecode_, which is a lower-level, platform-independent representation of the source code.

Python stores these compiled files to _speed up module loading_. The next time the program runs, Python loads the module from the compiled file _without recompiling it_, which improves performance.
