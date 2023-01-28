from ast import Pass


def main():
    a = str(input("Input: "))
    output = shorten(a)
    print("Output: " + output)

def shorten(word):
    def split(amaan):
        return [char for char in amaan]

    word = split(word)
    #print(tired)
    newa = []
    for i in range(len(word)):
    #   print(len(tired))

        vowel = ["a","A","e","E","I","i","O","o","U","u"]
        if word[i] not in vowel:

            newa.append(word[i])
        else:
            pass


            #print(tired)
    if type(newa) is list:

        newa = "".join(newa)
    return newa

if __name__ == "__main__":
    main()