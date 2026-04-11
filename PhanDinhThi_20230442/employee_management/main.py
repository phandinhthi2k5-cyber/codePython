from model.manager import Manager
from model.developer import Developer
from model.intern import Intern
from services.company import Company
from services.payroll import *
from utils.validators import *

company = Company()

# ================= ADD =================
def add_employee():
    try:
        emp_id = company.generate_id()
        name = input("Tên: ")

        age = int(input("Tuổi: "))
        validate_age(age)

        email = input("Email: ")
        validate_email(email)

        salary = float(input("Lương: "))
        validate_salary(salary)

        print("1.Manager 2.Developer 3.Intern")
        c = int(input("Chọn: "))

        if c == 1:
            emp = Manager(emp_id, name, age, email, salary)
        elif c == 2:
            lang = input("Ngôn ngữ: ")
            emp = Developer(emp_id, name, age, email, salary, lang)
        else:
            emp = Intern(emp_id, name, age, email, salary)

        company.add_employee(emp)
        print("✔ OK")

    except Exception as e:
        print("❌", e)

# ================= SHOW =================
def show_menu():
    try:
        print("1.Tất cả 2.Theo loại 3.Theo hiệu suất")
        c = int(input("Chọn: "))

        if c == 1:
            for e in company.list_all():
                print(e)
        elif c == 2:
            t = input("Nhập loại (Manager/Developer/Intern): ")
            for e in company.list_by_type(t):
                print(e)
        else:
            for e in company.sort_by_performance():
                print(e)

    except Exception as e:
        print("❌", e)

# ================= SEARCH =================
def search():
    try:
        print("1.ID 2.Tên 3.Ngôn ngữ")
        c = int(input())

        if c == 1:
            print(company.find_by_id(input()))
        elif c == 2:
            name = input()
            for e in company.employees:
                if name.lower() in e.name.lower():
                    print(e)
        else:
            lang = input()
            for e in company.employees:
                if hasattr(e, "language") and e.language == lang:
                    print(e)

    except Exception as e:
        print("❌", e)

# ================= SALARY =================
def salary_menu():
    print("Tổng:", total_salary(company))
    print("Top 3:")
    for e in top_3_salary(company):
        print(e)

# ================= PROJECT =================
def project_menu():
    try:
        print("1.Thêm 2.Xóa 3.Xem")
        c = int(input())

        emp = company.find_by_id(input("ID: "))

        if c == 1:
            emp.add_project(input("Tên dự án: "))
        elif c == 2:
            emp.remove_project(input("Tên dự án: "))
        else:
            print(emp.projects)

    except Exception as e:
        print("❌", e)

# ================= PERFORMANCE =================
def performance_menu():
    try:
        print("1.Cập nhật 2.Xuất sắc 3.Cần cải thiện")
        c = int(input())

        if c == 1:
            emp = company.find_by_id(input("ID: "))
            score = float(input("Điểm: "))
            if score < 0 or score > 10:
                raise ValueError("0-10")
            emp.performance = score

        elif c == 2:
            for e in company.employees:
                if e.performance > 8:
                    print(e)

        else:
            for e in company.employees:
                if e.performance < 5:
                    print(e)

    except Exception as e:
        print("❌", e)

# ================= HR =================
def hr_menu():
    try:
        print("1.Xóa 2.Tăng lương 3.Thăng chức")
        c = int(input())

        if c == 1:
            company.remove_employee(input("ID: "))

        elif c == 2:
            emp = company.find_by_id(input("ID: "))
            emp.base_salary *= 1.1

        else:
            emp = company.find_by_id(input("ID: "))
            if isinstance(emp, Intern):
                new = Developer(emp.emp_id, emp.name, emp.age, emp.email, emp.base_salary, "Python")
            else:
                new = Manager(emp.emp_id, emp.name, emp.age, emp.email, emp.base_salary)

            company.remove_employee(emp.emp_id)
            company.add_employee(new)

    except Exception as e:
        print("❌", e)

# ================= REPORT =================
def report():
    print("Tổng NV:", len(company.employees))
    print("Tổng lương:", total_salary(company))
    if company.employees:
        avg = sum(len(e.projects) for e in company.employees) / len(company.employees)
        print("Dự án TB:", avg)

# ================= MAIN =================
def main():
    while True:
        print("\n===== MENU =====")
        print("1.Thêm")
        print("2.Hiển thị")
        print("3.Tìm kiếm")
        print("4.Lương")
        print("5.Dự án")
        print("6.Đánh giá")
        print("7.Nhân sự")
        print("8.Báo cáo")
        print("9.Thoát")

        try:
            c = int(input("Chọn: "))

            if c == 1: add_employee()
            elif c == 2: show_menu()
            elif c == 3: search()
            elif c == 4: salary_menu()
            elif c == 5: project_menu()
            elif c == 6: performance_menu()
            elif c == 7: hr_menu()
            elif c == 8: report()
            elif c == 9: break

        except ValueError:
            print("❌ Nhập số")

if __name__ == "__main__":
    main()