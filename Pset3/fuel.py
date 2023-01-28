from multiprocessing.sharedctypes import Value


while True:

    try:
        fraction = input("Fraction: ")
        a,b = fraction.split("/")
        output = int(a)/int(b) * 100

        if output == 100:
            print("F")
            break
        elif output == 0:
            print("E")
            break
        elif output == 99:
            print("F")
            break
        elif output == 1:
            print("E")
            break
        elif output == 75:
            print("75%")
            break
        elif output == 50:
            print("50%")
            break
        elif output == 25:
            print("25%")
            break
        else:
            output = round(output)
            print(str(output) + "%")
            break
    except (ValueError,ZeroDivisionError):
        pass

