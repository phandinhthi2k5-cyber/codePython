cipher = {'a':'!', 'b':'@', 'c':'#', 'd':'$'}
# Hàm mã hóa
def encode(text):
    result = ""
    for ch in text:
        if ch in cipher:
            result += cipher[ch]
        else:
            result += ch  # giữ nguyên nếu không có trong bảng mã
    return result

# Hàm giải mã
def decode(text):
    # đảo ngược dictionary
    reverse_cipher = {v: k for k, v in cipher.items()}
    
    result = ""
    for ch in text:
        if ch in reverse_cipher:
            result += reverse_cipher[ch]
        else:
            result += ch
    return result
# Menu chương trình
while True:
    print("\n===== MENU =====")
    print("1. Mã hóa")
    print("2. Giải mã")
    print("0. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == "1":
        text = input("Nhập văn bản: ")
        print("Kết quả mã hóa:", encode(text))
        
    elif choice == "2":
        text = input("Nhập văn bản mã: ")
        print("Kết quả giải mã:", decode(text))
        
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Chọn sai!")
# Bảng mã

cipher = {'a':'!', 'b':'@', 'c':'#', 'd':'$'}


# Hàm mã hóa
def encode(text):
    result = ""
    for ch in text:
        if ch in cipher:
            result += cipher[ch]
        else:
            result += ch  # giữ nguyên nếu không có trong bảng mã
    return result

# Hàm giải mã
def decode(text):
    # đảo ngược dictionary
    reverse_cipher = {v: k for k, v in cipher.items()}
    
    result = ""
    for ch in text:
        if ch in reverse_cipher:
            result += reverse_cipher[ch]
        else:
            result += ch
    return result
# Menu chương trình
while True:
    print("\n===== MENU =====")
    print("1. Mã hóa")
    print("2. Giải mã")
    print("0. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == "1":
        text = input("Nhập văn bản: ")
        print("Kết quả mã hóa:", encode(text))
        
    elif choice == "2":
        text = input("Nhập văn bản mã: ")
        print("Kết quả giải mã:", decode(text))
        
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Chọn sai!")