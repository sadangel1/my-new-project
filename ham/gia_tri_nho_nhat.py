def gia_tri_nho_nhat(arr):
    temp = arr[0]
    for i in arr:
        if i <= temp: temp = i
    return temp

arr = [43,200,11,343,6536,234]
print(arr)
print("Giá trị nhỏ nhất "+ str(gia_tri_nho_nhat(arr)))