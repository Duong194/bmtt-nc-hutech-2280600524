def tinh_tong_so_chan(lst):
    tong=0
    for num in lst:
        if num%2==0:
            tong+=num
    return tong
input_list= input ("Nhap danh sach các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(",")]
tong_chan=tinh_tong_so_chan(numbers)
print(f"Tong cac so chan trong danh sach la:", tong_chan)