# pylint: disable=all

import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# Command line statement ---> py app.py -hello
