import math
a = float(input("Nhập cạnh a"))
b = float(input("Nhập cạnh b"))
c = float(input("Nhập cạnh c"))

s = (a+b+c)/2
area = math.sqrt(s* (s-a) * (s-b) * (s-b))

print("Diện tích",area)
