_a = int(input("Nhap vao so nguyen duong a: "))
_b = int(input("Nhap vao so nguyen duong b: "))
_c = int(input("Nhap vao so nguyen duong c: "))

if _a + _b > _c and _a + _c > _b and _b + _c > _a:
    print("Độ dài ba cạnh tam giác", _a, _b, _c)
else:
    print("Đây không phải là độ dài ba cạnh tam giác")