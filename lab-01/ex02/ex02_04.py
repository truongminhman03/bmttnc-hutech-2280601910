#Tạo 1 List rỗng để lưu kq
j = []
#duyệt qua all các số trong đoạn 2000 -3200, ktra xem i có chia hết cho 7 và ko phải bội của 5
for i in range(2000, 3201):
    if ( i % 7 ==0 ) and ( i % 5 != 0 ):
        j.append(str(i))
print(','.join(j))