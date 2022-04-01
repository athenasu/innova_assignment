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
        self.employees = []
        self.total_salary = 0
        self.managers = set()
        self.sorted_managers = {}

    def load_employees(self, json_filename: str) -> list[Employee]:
        try:
            with importlib.resources.open_text("resources", json_filename) as f:
                employees_list = json.load(f)
                for employee in employees_list:
                    CheckEmployeesJson(**employee)
                    self.employees.append(Employee(employee["id"],
                                                   employee["first_name"],
                                                   employee["manager"],
                                                   employee["salary"]))
                    if employee["manager"] is not None:
                        self.managers.add(employee["manager"])
            return self.employees
        except FileNotFoundError as e:
            print("File not found error")
            print(e)
        except json.JSONDecodeError as e:
            print("Wrong JSON format")
            print(e)
        except TypeError:
            raise TypeError("Type unexpected")

    def set_is_manager(self, employees: list[Employee]) -> None:
        for emp in employees:
            if emp.employee_id in self.managers:
                self.managers.remove(emp.employee_id)
                self.managers.add(emp)
                emp.set_is_manager(True)

    # recursive call that sorts the managers
    def sort_managers(self, manager_id, index: int):
        if index >= len(self.managers):
            return

        new_manager_id = 0
        for manager in self.managers:
            if manager.manager == manager_id:
                self.sorted_managers[manager.employee_id] = index
                new_manager_id = manager.employee_id
        self.sort_managers(new_manager_id, index + 1)
        return self.sorted_managers

    def find_manager(self, employees: list[Employee], manager_id: int) -> str:
        for employee in employees:
            if employee.employee_id == manager_id:
                return employee.first_name

    def find_member(self, employees: list[Employee], manager_id: int) -> list[str]:
        members = []
        for employee in employees:
            if employee.manager == manager_id:
                members.append(employee.first_name)
        return members

    def hierarchy(self, employees: list[Employee]):
        self.set_is_manager(employees)
        self.sort_managers(None, 0)
        for manager_id, index in self.sorted_managers.items():
            manager_name = self.find_manager(employees, manager_id)
            print("\t" * index + "Employees of: " + manager_name)
            members = self.find_member(employees, manager_id)
            members.sort()
            for member in members:
                member_index = index + 1
                print("\t" * member_index + member)

    def set_total_salary(self, employee_salary: list[Employee]) -> int:
        for emp in employee_salary:
            self.total_salary += emp.salary
        return self.total_salary
