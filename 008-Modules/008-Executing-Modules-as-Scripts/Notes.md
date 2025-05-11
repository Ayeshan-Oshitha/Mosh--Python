When we run a Python file directly, it is executed as the main program, and at that point, the name of the module is set to `__main__`. However, if we import that file as a module in another script, the name of the module will be the file's name (e.g., `sales` if the file is named sales.py).

This behavior allows us to use the same file both as a `script` (when run directly) and as a `reusable module` (when imported in other files).
