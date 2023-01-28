from re import A
import sys
import os
import csv
from wsgiref import headers
from tabulate import tabulate
def main():
    headers = []

    if control_input(sys.argv[1]):
        a = tabulates(sys.argv[1])
        for i in a[0]:
            headers.append(i)
            #print(headers)
        a.pop(0)
        print(tabulate(a, headers, tablefmt="grid"))
        #for i in a:


def control_input(word):
    if word.endswith(".csv") != True:
        print("Not a Csv file")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        return True

def tabulates(file_name):
    path = os.path.abspath(file_name)
    with open("{0}".format(path), newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data



if __name__ == "__main__":
    main()