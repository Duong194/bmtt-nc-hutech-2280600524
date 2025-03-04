def dao_nguoc_list(lst):
    return lst[::-1]
input_list= input ("Nhap danh sach các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(",")]
list_dao_nguoc=dao_nguoc_list(numbers)
print("Danh sach sau khi dao nguoc la:", list_dao_nguoc)