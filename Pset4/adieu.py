import inflect
p = inflect.engine()
namelist = []
adieu = "Adieu, adieu, to "
while True:
    try:

        names = input("")
        namelist.append(names)

    except EOFError:
        print(adieu + p.join(namelist,final_sep=","))
        break
