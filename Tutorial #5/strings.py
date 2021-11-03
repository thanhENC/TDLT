# import math

# while True:
#     num = int(input("Nhap mot so nguyen: "))
#     _sqrt = math.sqrt(num)
#     if _sqrt - round(_sqrt) == 0:
#         print(f"{num} la so chinh phuong.")
#     else:
#         print(f"{num} khong la so chinh phuong")
    
#     getChar = input("Tiep tuc hay khong Y/N: ")
#     if getChar.upper() == "Y":
#         break

# def calc(text):
#     text = text.replace('-', '+-')
#     numbers = text.split('+')
#     res = 0
    
#     for n in numbers:
#         res += int(n.strip().replace(' ', ''))

#     return res
    
# def remove_whitespace(text):
#     text = text.strip(" ")
#     while ("  " in text):
#         text = text.replace("  ", " ")
#     return text

# print("Chương trình xóa ký tự trắng thừa")
# text = input("Chuỗi: ")
# #result = remove_whitespace(str(text))
# result = text.replace("  "," ")
# print("Kết quả: " + ' '.join(text.split()))


# #Nhap diem 0-10
# import sys
# while True:
#     try:
#         m = float(input('Nhap diem '))
#         if m < 0 or m > 10:
#             print('Diem khong hop le!')
#         else:
#             print(f'Da ghi nhan diem: {m} diem.')
#             break
#     except:
#         print('Sai kieu du lieu!')


# #import module sys để gọi ra các ngoại lệ 
# import sys
# randomList = ['a', 0, 2]
# for nhap in randomList:
#     try:
#         print("phần tử: ", nhap)
#         r = 1/ int(nhap)
#         print("Kết quả với phần tử ", nhap, " là ", r)
#         break
#     except:
#         print("có ngoại lệ ", sys.exc_info()[0], " xảy ra.")
#         print("Nhập phần tử tiếp theo")
#         print()

# try:
#     x = int(input('Nhập một số trong khoảng 1-10: '))
#     if x < 1 or x > 10:
#         raise Exception
#     print('Ban vua nhap mot so hop le :D')
# except:
#     print('So ban vua nhap nam ngoai khoang cho phep mat roi!')

def GiaiPhuongTrinhBac1(a,b):
    if a==0 and b==0:
        return "Vô số nghiệm"
    elif a==0 and b!=0:
        return "Vô nghiệm"
    else:
        return "x = {0}".format(round(-b/a,2))

ketqua = GiaiPhuongTrinhBac1(4,9)
print(ketqua)

def XuatDuLieu(data):
    print(data)