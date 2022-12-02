num = input("Nhap so 1 - 7:")
if num.isnumeric() == False :
    print("Số không hợp lệ")
elif  int(num) > 7 or int(num) < 0:
     print("Số không hợp lệ")    
else:
    num = int(num)
    if num == 1: print("Chủ nhật")
    elif num == 2: print("Thứ 2")
    elif num == 3: print("Thứ 3")
    elif num == 4: print("Thứ 4")
    elif num == 5: print("Thứ 5")
    elif num == 6: print("Thứ 6")
    elif num == 7: print("Thứ 7")


#   Hoặc 

    #if num == 1: print("Chủ nhật")
    #else: print("Thứ "+str(num))
