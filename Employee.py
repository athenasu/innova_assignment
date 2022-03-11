'''
Employee class
'''


class Employee:

    def __init__(self, employee_id: int, first_name: str, manager: int, salary: int):
        self.employee_id = employee_id
        self.first_name = first_name
        self.manager = manager
        self.salary = salary

    def __str__(self):
        return f"id = {self.employee_id}, first_name = {self.first_name}, manager = {self.manager}, salary = {self.salary} "
