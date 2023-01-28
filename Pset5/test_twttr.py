from cgi import test
from twttr import shorten


def main():
    upper_lower()
    upp()


def upper_lower():
    assert shorten("umut") == "mt"
    assert shorten("UMUT") == "MT"
    assert shorten("UMut") == "Mt"
    assert shorten("666333") == "666333"
    assert shorten("3265") == "3265"
    assert shorten(",!?.") == ",!?."
    assert shorten("CS50P") == "CS50P"
def upp():
    assert shorten("CS50P") == "CS50P"


if __name__ == "__main__":
    main()