def format_employee(emp):
    return (
        f"ID: {emp.emp_id}\n"
        f"Tên: {emp.name}\n"
        f"Loại: {emp.__class__.__name__}\n"
        f"Tuổi: {emp.age}\n"
        f"Email: {emp.email}\n"
        f"Lương: {emp.calculate_salary()}\n"
        f"Hiệu suất: {emp.performance}\n"
        f"Dự án: {', '.join(emp.projects) if emp.projects else 'Không có'}\n"
        "---------------------------"
    )


def format_list(employees):
    if not employees:
        return "Không có dữ liệu"
    return "\n".join(format_employee(e) for e in employees)