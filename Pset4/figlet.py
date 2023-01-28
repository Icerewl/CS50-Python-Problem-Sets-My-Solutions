import sys
from pyfiglet import Figlet as fig

liste = ["slant","rectangles","alphabet"]
#if sys.argv[1] == "-f":
    #if sys.argv[2] in liste:
f = fig(font = sys.argv[2])
ex = input("Input: ")
print(f.renderText(ex))


    #else:
      #  sys.exit()
#else:
  # sys.exit()




