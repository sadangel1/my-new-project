num = input("Nhap so kiem tra:")
if num.isnumeric() == False:
    print("Lỗi")   
else:
    num = float(num)
    if num%2 == 0:
        print("Chẳn")
    elif num%2 != 0:
        print("Lẻ")    


   