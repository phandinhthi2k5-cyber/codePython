n = int(input("Nhập số nguyên: "))

if n > 10:
    print("Nhập vào số nguyên lớn hơn 10")
else:
    for _i in range(2, n + 1, 2):
        print(_i)
