'''
EmployeeBase class: employee_id, first_name, manager, salary
Setting properties and their setter methods
'''

from abc import ABC, abstractmethod


class EmployeeBase(ABC):

    def __init__(self, employee_id: int, first_name: str, manager: int, salary: int):
        self._employee_id = employee_id
        self._first_name = first_name
        self._manager = manager
        self._salary = salary

    # property and setters
    @property
    def employee_id(self) -> int:
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id) -> None:
        self._employee_id = employee_id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name) -> None:
        self._first_name = first_name

    @property
    def manager(self) -> int:
        return self._manager

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, salary) -> None:
        self._salary = salary

    @abstractmethod
    def __str__(self) -> str:
        return f"id = {self.employee_id}, first_name = {self.first_name}, " \
               f"manager = {self.manager}, salary = {self.salary} "
