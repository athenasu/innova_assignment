'''
Load employees JSON file, inject data into Employees class, add managers to managers set
Sets is_manager property in Employees class
Returns the top manager
Use employees dictionary and manager id to find team members
Print office hierarchy
'''


import importlib.resources

from src.entity.Employee import Employee
from src.service.CheckEmployeesJson import CheckEmployeesJson
import json


class EmployeeService:

    def __init__(self):
        self.employees = {}
        self.total_salary = 0
        self.managers = set()

    def load_employees(self, json_filename: str) -> dict[int, Employee]:
        try:
            with importlib.resources.open_text("resources", json_filename) as f:
                employees_list = json.load(f)
                for employee in employees_list:
                    check_point = CheckEmployeesJson(**employee)
                    if check_point.id:
                        self.employees[employee["id"]] = Employee(employee["id"],
                                                                  employee["first_name"],
                                                                  employee["manager"],
                                                                  employee["salary"])
                        if employee["manager"] is not None:
                            self.managers.add(employee["manager"])
            return self.employees
        except FileNotFoundError as e:
            print("File not found error")
            print(e)
        except json.JSONDecodeError as e:
            print("Wrong JSON format")
            print(e)

    def set_is_manager(self, employees: dict[int, Employee]) -> int:
        for emp_id, employee in employees.items():
            if emp_id in self.managers:
                employee.set_is_manager(True)
            if employee.is_top_manager:
                return employee.employee_id

    def find_top_manager(self, employees: dict[int, Employee], top_manager_id: int) -> str:
        for key, emp in employees.items():
            if emp.employee_id == top_manager_id:
                return emp.first_name

    def find_team_members(self, employees: dict[int, Employee], manager_id: int) -> list[str]:
        team_members = []
        for key, emp in employees.items():
            if manager_id == emp.manager:
                team_members.append(emp.first_name)
        team_members.sort()
        return team_members

    def print_hierarchy(self, employees: dict[int, Employee]) -> None:
        top_manager_id = self.set_is_manager(employees)
        top_manager_name = self.find_top_manager(employees, top_manager_id)
        tab = "\t"
        level = 1
        print(top_manager_name)
        print(top_manager_name + " is in charge of:")
        for emp_id, employee in employees.items():
            if employee.manager is top_manager_id:
                print(tab * level + employee.first_name)
                print(tab * level + employee.first_name + " is in charge of:")
                level += 1
                if employee.is_manager:
                    team_members = self.find_team_members(employees, emp_id)
                    for member in team_members:
                        print(tab * level + member)

    def set_total_salary(self, employee_salary: dict[int, Employee]) -> int:
        for key, emp in employee_salary.items():
            self.total_salary += emp.salary
        return self.total_salary
