from re import A
import sys
import os
import csv
from wsgiref import headers
from tabulate import tabulate

def main():
    headers = []
    abc = []

    if control_input(sys.argv[1]):
        a = tabulates(sys.argv[1])
        for i in a[0]:
            headers.append(i)
            #print(headers)
        a.pop(0)
        #first_second = a.split(",")
        #smtg = a(reversed(first_second))
        for i in a:
            bca = i[0].split(",")
            bca = list(reversed(bca))
            bca = ", ".join(bca)
            abc.append(bca)
            abc.append(i[1])


        abc = [abc[i:i+2] for i in range(0,len(abc),2)]
        for i in abc:
            i[0] = i[0][1:].lstrip()
        with open('after.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(headers)

            # write multiple rows
            writer.writerows(abc)


        #for i in a:



def control_input(word):
    if word.endswith(".csv") != True:
        print("Not a Csv file")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
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