import random


def main():
    level_a = get_level()
    abc_sit = generate_integer(level_a)
    if abc_sit == False:
        for i in range(9):
            generate_integer(level_a)
    else:
        pass
        #print("done")

def get_level():
    while True:
        try:
            levela = int(input("Level: "))
            if 4 > levela > 0:
                return levela
        except ValueError:
            pass


def generate_integer(level_b):
    wrongTimes = 0
    countAS = -1
    if level_b == 1:
        level_b = 9
        lower__limit = 0
    if level_b == 2:
        level_b = 99
        lower__limit = 10
    if level_b == 3:
        level_b = 999
        lower__limit = 100

    a,b = random.randint(lower__limit, level_b),random.randint(lower__limit, level_b)
    while True:
        countAS += 1
        if countAS == 10:
            return True
        try:
            input_a = int(input("{0} + {1} = ".format(a,b)))
            if input_a != a + b:

                wrongTimes += 1
                print("EEE")
                if wrongTimes == 3:
                    print("{0} + {1} = {2}".format(a,b,a+b))
                    return False
                pass

            else:

                return False

        except ValueError:

            pass


if __name__ == "__main__":
    main()