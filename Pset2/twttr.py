from re import A


tired = input("Input: ")

def split(word):
    return [char for char in word]

tired = split(tired)
#print(tired)
for i in range(-1,len(tired)):
 #   print(len(tired))
    try:
        if tired[i] == "a" or tired[i] == "A" or tired[i] == "e" or tired[i] == "E" or tired[i] == "o" or tired[i] == "O" or tired[i] == "u" or tired[i] == "U" or tired[i] == "I" or tired[i] == "i":

            tired.pop(i)
            #print(tired)
    except:
        pass
    
tired = "".join(tired)
print("Output: " + tired)