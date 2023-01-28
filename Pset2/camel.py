rihanna = input("camelCase: ")

def split(word):
    return [char for char in word]

jayz = split(rihanna)

for i in range(len(jayz)):
    if jayz[i].isupper():
        
        jayz.insert(i,"_")
        a = jayz[i+1].lower()
        jayz.pop(i+1)

        jayz.insert(i+1,a)
        
        
    else:
        pass    
        
kanye = "".join(jayz).lower()
print("snake_case: " + kanye)        