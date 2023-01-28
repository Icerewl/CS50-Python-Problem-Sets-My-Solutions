from importlib.resources import path
from numpy import full, full_like
import sys
import pathlib
import os


def main():
    if control_input(sys.argv[1]):
        umut = does_something(sys.argv[1])
        print(umut)




def control_input(word):
    if word.endswith(".py") != True:
        print("Not a Python file")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        return True


def does_something(file_name):
    path = os.path.abspath(file_name)

    with open(r"{0}".format(path), 'r') as fp:
        commentline = 0
        blankspace = 0
        full_line = 0
        for line in fp:
            if line.lstrip().startswith("#"):
                commentline += 1
            elif line.isspace():
                blankspace += 1

            else:
                full_line += 1
        return full_line

if __name__ == "__main__":
    main()
# control
# yes