from string import punctuation
def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def split(word):
    return [char for char in word]

def is_valid(s):
    s = split(s)
    punctuations = [w for w in s if w in punctuation]
    state = True
    situation = True
    a = 0
    for i in s:
        if i in {"1","2","3","4","5","6","7","8","9","0"} and state:
            if i == "0":
                return False
            else:
                state = False
                pass

    #Misunderstood the assignment but still it worked
    if all([item.isalpha() for item in s]):
        situation = False
        pass
    else:


        if not s[0].isalpha() or not s[1].isalpha():
            return False
        else:
            if s[-1].isalpha() or s[-2].isalpha() and situation: #problem
                return False
            else:
                if len(punctuations) > 0:
                    return False
                else:
                    return True



main()