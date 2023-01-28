def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    withoutsign = float(d.replace('$',''))
    #print(withoutsign)
    #print(type(withoutsign))
    floatdollars = float(withoutsign)
    return floatdollars


def percent_to_float(p):
    
    percentage = float(p.strip("%")) / 100
    #print(percentage)
    #print(type(percentage))
    return percentage


main()