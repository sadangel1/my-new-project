import re


def dem_so_lan(chuoi):
    chuoi = chuoi.lower()
    arr = chuoi.split()
    KetQua = {}
    for i in arr:
        if i in KetQua:
            KetQua[i] = KetQua[i]+1
        else :
            KetQua[i] = 1    
    return KetQua
str = input("Nhập chuỗi cần đếm: ")
print(dem_so_lan(str))