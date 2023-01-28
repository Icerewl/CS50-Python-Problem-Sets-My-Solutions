from plates import is_valid

def main():
    test_cs50()
    test_ecto88()
    test_cs05()
    test_cs50p2()
    test_pi()
    test_H()


def test_cs50():
    assert is_valid("CS50") == True
def test_ecto88():
    assert is_valid("ECTO88") == True
def test_cs05():
    assert is_valid("CS05") == False
def test_cs50p2():
    assert is_valid("CS50P2") == False
def test_pi():
    assert is_valid("PI3.14") == False
def test_H():
    assert is_valid("H") == False

if __name__ == "__main__":
    main()