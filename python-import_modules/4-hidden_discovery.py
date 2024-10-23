#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Specify the path to the compiled module
    module_path = '/tmp/hidden_4.pyc'

    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get the list of all names defined by the module
    names = dir(hidden_4)

    # Filter out names that start with '__' and print them in alpha order
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)