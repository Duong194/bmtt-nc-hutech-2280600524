def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str=input("Nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ",dao_nguoc_chuoi(input_str))