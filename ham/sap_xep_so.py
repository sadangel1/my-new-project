def so_lon_nhat(num1,num2,num3) :
    temp = 0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return num1,num2,num3
so1 = input("Nhập số 1: ")
so2 = input("Nhập số 2: ")
so3 = input("Nhập số 3: ")
print(so_lon_nhat(so1,so2,so3))
