from ast import Pass
from audioop import reverse
from multiprocessing.sharedctypes import Value


months = {
    "1":"January",
    "2":"February",
    "3":"March",
    "4":"April",
    "5":"May",
    "6":"June",
    "7":"July",
    "8":"August",
    "9":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}
reverse_months = {v: k for k, v in months.items()}

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            date = date.strip()
            a,b,c = date.split("/")
            if int(a) > 12:
                raise ValueError()
            if len(a) > 2:
                raise ValueError()
            if int(b) > 30:
                raise ValueError()
        elif " " in date:
            a,b,c = date.split(" ")
            if len(b) > 2:
                raise ValueError()
            if int(b.rstrip(b[-1])) > 30:
                raise ValueError()


        elif "-" in date:
            a,b,c = date.split("-")
        #if sayı month içindeyse value yu ver yoksa reverse monthun içindeki valueyi ver
        if len(a) > 2:
            b = b.rstrip(b[-1])
            if len(b) == 1:
                b = "0" + b
            if len(reverse_months[a]) == 1:
                reverse_months[a] = "0" + reverse_months[a]
            print(c + "-" + reverse_months[a] + "-" + b)
            exit(1)

        else:
            if len(b) == 1:
                b = "0" + b
            if len(a) == 1:
                a = "0" + a
            print(c + "-" + a + "-" + b)
            exit(1)
    except ValueError:
        pass





