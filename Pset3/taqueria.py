total = 0
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
menulower = {k.lower(): v for k, v in menu.items()}
a = 0
item = ""
while True:

    try:

        item = input("Item: ")
        itemlower = item.lower()
        if item in menu:
            total = menu[item] + total
            print ("Total: $%.2f" % float(total))
            a = 1

        if  itemlower in menulower and a == 0:
            total = menulower[itemlower] + total
            print ("Total: $%.2f" % float(total))


    except EOFError:
        break