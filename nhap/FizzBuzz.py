x = int(input("nhap so bat dau: "))
y = int(input("nhap so ket thuc: "))
char = ""
for i in range(x,y):
    if(int(i) % 3 == 0 and int(i)%5 == 0):
        char += 'FizzBuzz'
    if(int(i) % 3 == 0):
        char += 'Fizz'
    elif(int(i)  % 5 == 0):
        char += 'Buzz'
    else:
        char +=  str(i)
print(char)