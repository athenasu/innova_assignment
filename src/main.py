'''
Read employees.json file from resources package
Render office hierarchy and total salary
'''

from src.service.EmployeeService import EmployeeService


def print_hierarchy():
    files = range(1, 6)
    start_print = True
    while start_print:
        json_file = int(input("Type employees file to check (1-5): "))
        if json_file in files:
            service = EmployeeService()
            employees = service.load_employees(f"employees{json_file}.json")
            service.hierarchy(employees)
            total_salary = format(service.set_total_salary(employees), ",")
            print(f"Total salary: {total_salary}")
            start_print = False
        else:
            print("Please select from file 1-5")


if __name__ == "__main__":
    print_hierarchy()
