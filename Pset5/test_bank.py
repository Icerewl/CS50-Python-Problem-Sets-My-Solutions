from bank import value

def main():
    test_hello()
    test_hello_what()
    test_hello_newman()
    test_hello_how()


def test_hello():
    assert value("Hello") == 0
def test_hello_newman():
    assert value("Hello, Newman") == 0
def test_hello_how():
    assert value("How you doing?") == 20
def test_hello_what():
    assert value("What's happening?") == 100

if __name__ == "__main__":
    main()