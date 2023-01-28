from multiprocessing.sharedctypes import Value
def main():
    inp_a = input("Fraction: ")
    converted_inp = convert(inp_a)
    last = gauge(converted_inp)
    print(last)
    return last
def convert(fraction):


    a,b = fraction.split("/")
    if b == 0:
        raise ZeroDivisionError
    elif a > b:
        raise ValueError





    output = int(a)/int(b) * 100
    output = round(output)
    return output

def gauge(percantage):
        if percantage == 100:
            return "F"

        elif percantage == 0:
            return "E"

        elif percantage == 99:
            return "F"

        elif percantage == 1:
            return "E"

        elif percantage == 75:
            return "75%"
        elif percantage == 50:
            return "50%"
        elif percantage == 25:
            return "25%"
        else:
            percantage = round(percantage)
            x = str(percantage) + "%"
            return x

if __name__ == "__main__":
    main()
