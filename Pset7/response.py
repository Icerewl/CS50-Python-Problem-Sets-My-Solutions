
from validator_collection import validators, checkers, errors

def main():
    condition = input("What's your email address? ")
    try:
        email_address = validators.email(condition, allow_empty = False)
        print("Valid")

    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()