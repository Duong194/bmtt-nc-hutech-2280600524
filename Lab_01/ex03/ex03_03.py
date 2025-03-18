def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list= input ("Nhap danh sach các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(",")]
my_tuple=tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)