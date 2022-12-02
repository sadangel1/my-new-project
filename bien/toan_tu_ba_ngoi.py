num = input("Nhap so kiem tra:")
if num.isnumeric() == False:
    print("Lỗi")
else:
    num = int(num)
    print("Chẳn" if num % 2 == 0 else "Le")


