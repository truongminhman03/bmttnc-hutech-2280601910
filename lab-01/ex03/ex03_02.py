def dao_nguoc_list(lst):
    return lst[::-1]
#Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm và in ra kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược là:", list_dao_nguoc)