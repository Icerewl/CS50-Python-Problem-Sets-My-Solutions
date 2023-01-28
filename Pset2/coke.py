
from numpy import insert



cokeprice = 50
while True:
    print("Amount Due: " + str(cokeprice))
    insertedCoin = input("Insert coin: ")

    
    

    #print(type(insertedCoin))
    #print(insertedCoin)
    #print(type(cokeprice))
    if insertedCoin == "25":
        cokeprice = cokeprice - 25
    elif insertedCoin == "10":
        cokeprice = cokeprice - 10
    elif insertedCoin == "5":
        cokeprice = cokeprice - 5
    
    
    if cokeprice < 0 or cokeprice == 0:

        #cokeprice = cokeprice + abs(cokeprice) * 2
        print("Change owed: " + str(abs(cokeprice)))
        break
    else: 
        pass