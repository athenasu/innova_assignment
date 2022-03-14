'''
Read employees.txt file
Render office hierarchy
'''
import json
from Employee import Employee

# LOAD JSON FILE
with open("employees.json") as f:
    data = json.load(f)


# RETURNS LIST OF EMPLOYEES
def add_employee(data: json):
    employees_list = {}
    for employee in data:
        employees_list.setdefault(employee["id"], Employee(employee["id"], employee["first_name"], employee["manager"],
                                                           employee["salary"]))
    return employees_list


# RETURNS EMPLOYEE HIERARCHY DICTIONARY
def employees_hierarchy(employees: dict[int, Employee]):
    manager_employee = {}

    for id, employee in employees.items():
        if employee.manager is not None:
            manager_employee.setdefault(employee.manager, [])
            manager_employee[employee.manager].append(employee.first_name)

    return manager_employee


# RETURNS TOTAL SALARY
def calc_total_salary(employees: dict[int, Employee]):
    total_salary = 0
    for id, employee in employees.items():
        total_salary += employee.salary

    print(f"Total salary: {total_salary}")


def print_hierarchy(hierarchy_dict: dict, employees: dict[int, Employee]):
    for id, employee in employees.items():
        if id in hierarchy_dict.keys():
            hierarchy_dict[employee.first_name] = hierarchy_dict.pop(id)

    for key, employee_list in hierarchy_dict.items():
        print(f"Employees of: {key}")
        for employee in employee_list:
            print("\t" + employee)


# CALLING FUNCTIONS
employees = add_employee(data)
hierarchy_dict = employees_hierarchy(employees)
print_hierarchy(hierarchy_dict, employees)
calc_total_salary(employees)
