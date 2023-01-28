from cgi import test
from numb3rs import validate


def main():
    test_upper_lower()
    test_upp()
    test_firstbyte()


def test_upper_lower():
    assert validate(r"0.0.0.0") == True
    assert validate(r"0.0.0") == False
    assert validate(r"0.0") == False
    assert validate(r"0") == False

def test_upp():
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
def test_firstbyte():
    assert validate("2") == False



if __name__ == "__main__":
    main()