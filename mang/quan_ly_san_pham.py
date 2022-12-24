data = []

def add(item):
    data.append(item)

def update(index,item):
    data[index] = item


def print_data():
    print(data)

def find(id):
    result = -1
    for i,item  in enumerate(data):
        if item['id'] == id:
            result =  i
            break
    return result


def delete(index):
    del data[index]
        

print("What do you want to do? -\n"\
        "0. List\n" \
        "1. Add\n" \
        "2. Edit\n" \
        "3. Delete\n" \
        "4. Exit\n" 
        )
while True:
    option = int(input("Select option 0 or 4: "))
    if option == 0:
        print_data()
    if option == 1:
        id = int(input("Nhập id: "))
        str_name = input("Nhập tên: ")
        str_qty = input("Nhập số lượng: ")
        add({'name': str_name, 'id': id, 'qty': str_qty})
        print_data()
    if option == 2:
        id = int(input("Nhập mã sản phẩm sửa: "))
        index = find(id) 
        if index != -1 :
            str_name = input("Nhập tên: ")
            str_qty = input("Nhập số lượng: ")
            update(index,{'name': str_name, 'id': id, 'qty': str_qty})
        else:
            print("Không tìm thấy")
    if option == 3:
        id = int(input("Nhập id xóa: "))
        index = find(id) 
        if index != -1 :
            delete(index)
        else:
            print("Không tìm thấy")
    elif option == 4:
        break

