chieuCao = input("Nhập chiều cao (m): ")
canNang = input("Nhập cân nặng (kg): ")

def is_float_digit(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False

if is_float_digit(chieuCao) == False :
    print("Chiều cao không hợp lệ")
elif is_float_digit(canNang) == False :
    print("Cân nặng không hợp lệ")
elif float(chieuCao) == 0 or float(canNang) == 0:
    print("Không hợp lệ")    
else:
    bmi = float(canNang) / (float(chieuCao) * float(chieuCao))
    msg = "Gầy cấp độ III"
    if bmi >= 16 and bmi < 17 : msg = "Gầy cấp độ II"
    if bmi >= 17 and bmi < 18.5 : msg = "Gầy cấp độ I"
    if bmi >= 18.5 and bmi < 25 : msg = "Bình thường"
    if bmi >= 25 and bmi < 30 : msg = "Thừa cân"
    if bmi >= 30 and bmi < 35  : msg = "Béo phì cấp độ I"
    if bmi >= 35 and bmi < 40 : msg = "Béo phì cấp độ II"
    if bmi >= 40 : msg = "Béo phì cấp độ III"

    print("Số bmi là {b}. Kết quả {k}".format(b=bmi,k=msg))
    

     