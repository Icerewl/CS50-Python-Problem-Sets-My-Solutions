greeting = input("Greeting: ")
greeting = greeting.strip()
if greeting.startswith("Hello"):
    print("$0")

elif greeting.startswith("H") == False:
    print("$100")

elif greeting.startswith('H') != "Hello":
    print("$20")

