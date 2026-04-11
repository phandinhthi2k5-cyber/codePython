def total_salary(company):
    return sum(e.calculate_salary() for e in company.employees)

def top_3_salary(company):
    return sorted(company.employees, key=lambda e: e.calculate_salary(), reverse=True)[:3]