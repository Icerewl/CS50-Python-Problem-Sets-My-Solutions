guess = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
#problems
guess = guess.strip()
guess = guess.lower()
if guess == "forty two":
    print('Yes')
elif guess == "42":
    print('Yes')
elif guess == "forty-two":
    print('Yes')
else:
    print('No')