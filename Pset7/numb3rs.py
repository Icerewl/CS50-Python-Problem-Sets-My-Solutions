


import re
import sys

def main():
    ip_address = input("IPv4 Address: ").strip()
    if validate(ip_address):
        print("True")
    else:
        print("False")


def validate(ip_adress):
    if re.search(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]', str(ip_adress)):
        ip_adress = ip_adress.split(".")
        count = 0
        for i in ip_adress:
            if 0 <= int(i) <= 255:
                count += 1
            else:
                pass
        if count == 4:
            return True
        else:
            return False
    else:
        return False






if __name__ == "__main__":
    main()