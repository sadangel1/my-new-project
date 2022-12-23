from typing import Match


import random

nguoiChoiHienTai = random.randint(0,1)
nguoiThua = 0
so_nhap = 0
so_diem = 0
myDict = {0:"Human",1:"Computer"}
print("Người bắt đầu là " + myDict[nguoiChoiHienTai])
while True:
    
    if(nguoiChoiHienTai == 0):
        so_nhap = int(input("Nhập từ 1 đến 3: "))
        if so_nhap > 3:
            print("ăn gian")
            break
    elif(nguoiChoiHienTai == 1):  
         so_nhap = random.randint(1,3)
    so_diem += so_nhap     
    print("Điểm hiện tại của {b} là {a}".format(a=so_nhap,b =myDict[nguoiChoiHienTai] ))
    print("Tổng điểm {a}".format(a=so_diem ))
    if so_diem > 21:
        nguoiThua = nguoiChoiHienTai
        print("Kết thúc {a}. Người thua là {b}".format(a=so_diem, b =myDict[nguoiChoiHienTai] ))
        break
    nguoiChoiHienTai = 1 if nguoiChoiHienTai ==0 else 0    
    