from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        for e in self.employees:
            if e.emp_id == emp.emp_id:
                raise DuplicateEmployeeError()
        self.employees.append(emp)

    def generate_id(self):
        return str(len(self.employees) + 1)

    def find_by_id(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id)

    def remove_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        self.employees.remove(emp)

    def list_all(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return self.employees

    def list_by_type(self, t):
        return [e for e in self.employees if e.__class__.__name__ == t]

    def sort_by_performance(self):
        return sorted(self.employees, key=lambda e: e.performance, reverse=True)