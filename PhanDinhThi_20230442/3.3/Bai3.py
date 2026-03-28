import time

nam_sinh = int(input("Nhap vao nam sinh: "))
x = time.localtime()
nam_hien_tai = x[0]
tuoi = nam_hien_tai - nam_sinh
print("Năm sinh", nam_sinh, "tuổi của bạn là", tuoi, "tuổi")