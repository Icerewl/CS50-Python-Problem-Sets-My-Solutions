import requests
import sys
import math
if 0 <  float(sys.argv[1]) < 10:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        amount = r.json()
        print(amount["bpi"]["USD"])
        amount = str(float(amount["bpi"]["USD"]["rate_float"]) * float(sys.argv[1]))
        amount = amount[:2] + "," + amount[2:]

        print("$" + amount)

    except requests.RequestException:
        pass



