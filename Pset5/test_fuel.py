import fuel
import pytest
def main():
    test_three()
    test_one()
    test_two()
    test_hundred()
    test_zerodivision()
    test_aisbigger()


def test_three():
    assert fuel.convert("3/4") == 75 and fuel.gauge(75) == "75%"
def test_one():
    assert fuel.convert("2/3") == 67 and fuel.gauge(67) == "67%"
def test_two():
    assert fuel.convert("100/100") == 100 and fuel.gauge(100) == "F"
def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")
def test_aisbigger():
    with pytest.raises(ValueError):
        fuel.convert("3/2")
def test_hundred():
    assert fuel.convert("1/100") == 1 and fuel.gauge(1) == "E"


if __name__ == "__main__":
    main()