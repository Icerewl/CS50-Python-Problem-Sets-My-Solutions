liste = {}

while True:

    try:
        item = input("")
        if item in liste:
            liste[item] = liste.get(item,0) + 1
            #print(liste)
        else:

            liste[item] = 1


            #if i == item:
             #   liste[item] += 1
              #  print(liste)
               # print("1")
            #else:
             #
              #  print(liste)
               # print("2")





    except (EOFError,KeyError):
        a = 0
        for i in liste:
            print(str(liste[i]) + " " + str(i).upper())
        break