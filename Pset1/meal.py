time = input("Time: ")
# 78   11 12  18 19

septime = time.split(":")
septime1 = ''.join(septime)
septime1 = float(septime1)

#print(septime1)

if septime1 > 699 and septime1 < 801:
    print("breakfast time")

elif septime1 > 1199 and septime1 < 1301:
    print("lunch time")

elif septime1 > 1799 and septime1 < 1901:
    print("dinner time")

else:
    print()