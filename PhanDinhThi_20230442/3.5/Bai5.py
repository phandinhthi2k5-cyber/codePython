import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Kiểm tra
if a == 0:
    print("Đây không phải là phương trình bậc hai")
    if b != 0:
        x = -c / b
        print("Phương trình có một nghiệm: x =", x)
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
else:
    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        print("Phương trình vô nghiệm")