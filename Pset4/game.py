import random

while True:

    try:
        level = int(input("Level: "))
        val = int(level)
        if 1000 > val > 0:
            while True:
                guess = int(input("Guess: "))
                try:
                    val = guess
                    if 100 > val > 0:
                        chosen_level = random.randint(1,int(level))
                        while True:
                            if guess > chosen_level:
                                print("Too large!")
                                raise ValueError
                            elif guess < chosen_level:
                                print("Too small!")
                                raise ValueError
                            else:
                                print("Just right!")
                                exit(1)
                    else:
                        break
                except ValueError:
                    pass
        else:

            break
    except ValueError:
         pass




