data = {}
import collections
import json
class SinhVien:

    def get_sv_by_ma_sinh_vien(self, id):
        result = -1
        for k, v in data.items():
            if k == id:
                result = 1
                self.ma_sinh_vien = v['ma_sinh_vien']
                self.ho_ten = v['ho_ten']
                self.name_sinh = v['name_sinh']
                self.que_quan = v['que_quan']
                self.chuyen_nganh = v['chuyen_nganh']
                self.lop = v['lop']
                break
        return result
    def update(self):
        data[self.ma_sinh_vien] = {'ma_sinh_vien':self.ma_sinh_vien,'ho_ten':self.ho_ten,'name_sinh':self.name_sinh,'que_quan':self.que_quan,'chuyen_nganh':self.chuyen_nganh,'lop':self.lop}
    def show(self):
        print(data[self.ma_sinh_vien])
    def add(self):
        data[self.ma_sinh_vien] = {'ma_sinh_vien':self.ma_sinh_vien,'ho_ten':self.ho_ten,'name_sinh':self.name_sinh,'que_quan':self.que_quan,'chuyen_nganh':self.chuyen_nganh,'lop':self.lop}
    def delete(self):
        del data[self.ma_sinh_vien] 
    def sort(self):

        items = data.items()
        print(collections.OrderedDict(sorted(items)))

    def get_all(self):
        print(data)
    def tim_kiem(self,tu_khoa):
        result = -1
        for k, v in data.items():
            if v['ho_ten'] == tu_khoa or v['ma_sinh_vien'] == tu_khoa:
                result = 1
                self.ma_sinh_vien = v['ma_sinh_vien']
                self.ho_ten = v['ho_ten']
                self.name_sinh = v['name_sinh']
                self.que_quan = v['que_quan']
                self.chuyen_nganh = v['chuyen_nganh']
                self.lop = v['lop']
                break
        return result



print("What do you want to do? -\n"\
        "0. List\n" \
        "1. Add\n" \
        "2. Edit\n" \
        "3. Delete\n" \
        "4. Search\n" \
        "5. Sort\n" \
        "6. Exit\n" 
        )
while True:
    option = int(input("Select option 0 or 6: "))
    if option == 0:
        sv = SinhVien()
        sv.get_all()
    if option == 1:
        sv = SinhVien()
        ma_sinh_vien =  input("M?? sinh vi??n: ")
        kq = sv.get_sv_by_ma_sinh_vien(ma_sinh_vien) 
        
        if kq == -1 :
            sv.ma_sinh_vien =ma_sinh_vien
            sv.ho_ten = input("H??? t??n: ")
            sv.name_sinh = input("N??m sinh: ")
            sv.que_quan = input("Qu?? qu??n: ")
            sv.chuyen_nganh = input("Chuy??n ng??nh: ")
            sv.lop = input("l???p: ")
            sv.add()
            sv.show()
        else:
            print("???? t???n t???i")
    if option == 2:
        sv = SinhVien()
        ma_sinh_vien = input("M?? sinh vi??n s???a: ")
        kq = sv.get_sv_by_ma_sinh_vien(ma_sinh_vien) 
        if kq != -1 :
            sv.ho_ten = input("H??? t??n: ")
            sv.name_sinh = input("N??m sinh: ")
            sv.que_quan = input("Qu?? qu??n: ")
            sv.chuyen_nganh = input("Chuy??n ng??nh: ")
            sv.lop = input("l???p: ")
            sv.update()
            sv.show()
        else:
            print("Kh??ng t??m th???y")
    if option == 3:
        sv = SinhVien()
        ma_sinh_vien = (input("M?? sinh vi??n x??a: "))
        kq = sv.get_sv_by_ma_sinh_vien(ma_sinh_vien) 
        if kq != -1 :
            sv.delete()
            sv.get_all()
        else:
            print("Kh??ng t??m th???y")
    if option == 4:
        sv = SinhVien()
        tk = (input("Nh???p t??? kh??a c???n t??m: "))
        kq = sv.tim_kiem(tk) 
        if kq != -1 :
            sv.show()
        else:
            print("Kh??ng t??m th???y")
    if option == 5:
        sv = SinhVien()
        sv.sort()
 
    elif option == 6:
        break


        


