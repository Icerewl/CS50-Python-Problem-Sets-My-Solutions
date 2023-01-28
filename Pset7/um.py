from posixpath import split
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    split = re.findall(r"(?<![a-zA-Z])(um|Um|UM)(?![a-zA-Z])",s)
    return len(split)



if __name__ == "__main__":
    main()