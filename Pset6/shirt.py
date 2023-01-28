from email.mime import image
from re import A
import sys
import os
import csv
from wsgiref import headers
from tabulate import tabulate
from PIL import Image,ImageOps,ImageFilter
def main():

    if control_input(sys.argv[1],sys.argv[2]):
        tabulates(sys.argv[1])


def control_input(word,word2):
    if word[-3:] != word2 [-3:]:
        print("Extensions must be same")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        if word.endswith(".png") or word.endswith(".jpg") or word.endswith(".jpeg") and word2.endswith(".png") or word2.endswith(".jpg") or word2.endswith(".jpeg"):
            return True
        else:
            print("hololo")
            sys.exit(1)

def tabulates(puppet):
    puppet = Image.open(puppet)
    shirt = Image.open("shirt.png")

    size = shirt.size
    #shirt = shirt.convert("RGBA")
    puppet = ImageOps.fit(puppet, size=size)
    puppet.paste(shirt,shirt)
    #puppet.show()
    puppet.save(sys.argv[2])





if __name__ == "__main__":
    main()