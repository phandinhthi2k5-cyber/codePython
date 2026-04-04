# Hàm sum
def tinh_tong_sum():
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tong = sum(_list)
    print("Tổng (dùng sum) =", tong)

# Dùng for
def tinh_tong_for():
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tong = 0
    for x in _list:
        tong = tong + x
    print("Tổng (dùng for) =", tong)

# Dùng while
def tinh_tong_while():
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tong = 0
    i = 0
    while i < len(_list):
        tong = tong + _list[i]
        i += 1
    print("Tổng (dùng while) =", tong)

while True:
    print("\n===== MENU =====")
    print("1. Tính tổng (sum)")
    print("2. Tính tổng (for)")
    print("3. Tính tổng (while)")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        tinh_tong_sum()
    elif chon == "2":
        tinh_tong_for()
    elif chon == "3":
        tinh_tong_while()
    elif chon == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Chọn sai, nhập lại!")