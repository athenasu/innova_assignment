'''
Read employees.json file from resources package
Render office hierarchy and total salary
'''

from src.service.EmployeeService import EmployeeService


def print_hierarchy():
    files = ["1", "2"]
    start_print = True
    while start_print:
        json_file = input("Type employees file to check (1 or 2): ")
        if json_file in files:
            service = EmployeeService()
            employees = service.load_employees("employees" + json_file + ".json")
            total_salary = format(service.set_total_salary(employees), ",")
            service.print_hierarchy(employees)
            print(f"Total salary: {total_salary}")
            start_print = False
        else:
            print("Please select from file 1 or 2")


if __name__ == "__main__":
    print_hierarchy()
