def main():
    inputas = input("Greeting: ")
    print(value(inputas))


def value(greeting):
    if greeting.startswith("Hello"):
        return 0

    elif greeting.startswith("H") == False:
        return 100

    elif greeting.startswith('H') != "Hello":
        return 20


if __name__ == "__main__":
    main()





