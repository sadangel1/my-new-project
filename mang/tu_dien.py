arr = [{'en':'house','vi' : 'Nhà'},{'en':'tree','vi' : 'Cây'},{'en':'pencil','vi' : 'Bút chì'},{'en':'car','vi' : 'Xe hơi'}]


def tra_cuu (tu_tra):
    tu_tra.lower()
    ketqua = "Không tìm thấy"
    for v in arr:
        if v['en'] == tu_tra:
            ketqua = v['vi']
    return ketqua

print("Nhập từ cần tra")

while True:
    str = input("Nhập tiếng anh: ")
    print(tra_cuu(str))
    
