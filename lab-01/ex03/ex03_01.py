def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
#Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm và in ra kqua
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong List là:", tong_chan)