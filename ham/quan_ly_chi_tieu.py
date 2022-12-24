data = []
def add(item):
    data.append(item)
    
def find(value):
    result = -1
    for i in range(len(data)):
        if data[i]['name'] == value:
            result =  i
            break
    return result

def delete(value):
    result = find(value)
    if(result != -1):
        del data[result]

print("What do you want to do? -\n"\
        "1. Add\n" \
        "2. Remove")
while True:
    option = int(input("Select option 1 or 2: "))
    if option == 1:
        str_name = input("Nhập tên: ")
        str_amount = input("Nhập tiền: ")
        str_date = input("Nhập ngày: ")
        add({'name': str_name, 'amount': str_amount, 'date': str_date})
        print(data)
    if option == 2:
        str_name = input("Nhập tên muốn bỏ: ")
        delete(str_name)
        print(data)
    elif option != 1 and option !=2:
        break

