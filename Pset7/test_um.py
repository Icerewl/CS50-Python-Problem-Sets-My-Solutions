from um import count
def main():

    test_umma()
    test_imma()


def test_umma():

    assert count("um") == 1
    assert count("um?") == 1

def test_imma():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


if __name__ == "__main__":
    main()