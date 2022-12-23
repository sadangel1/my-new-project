x = int(input("nhap chieu cao: "))
y = int(input("nhap chieu dai: "))
char = input("nhap ky tu")

for i in range(1, x+1 ):
    text = ""
    for j in range(1,y + 1 ):
        if(i not in[1,x] and j not in[1,y]):
            text += " "
        else:
            text += char
    print(text)
    
    


