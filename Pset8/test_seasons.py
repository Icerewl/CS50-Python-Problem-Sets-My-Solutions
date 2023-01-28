
import pytest
from seasons import check_date



def main():
    test_this()
    test_that()



def test_this():
    assert check_date("2021-08-12") == True


def test_that():
    assert check_date("2022-08-12") == True

def test_error():

    with pytest.raises(SystemExit):
        check_date("2021.0.12")




if __name__ == "__main__":
    main()