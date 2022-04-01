'''
Employee class: employee_id, first_name, manager, salary
Setting properties and their setter methods
'''

from src.entity.EmployeeBase import EmployeeBase


class Employee(EmployeeBase):

    def __init__(self, employee_id: int, first_name: str, manager: int, salary: int):
        super().__init__(employee_id, first_name, manager, salary)
        self._is_top_manager = False
        self.is_manager = False

    # property and setters
    @property
    def is_top_manager(self):
        return self._is_top_manager

    # @property
    # def is_manager(self) -> bool:
    #     return self.is_manager
    #
    # @is_manager.setter
    # def is_manager(self, is_manager: bool) -> None:
    #     self.is_manager = is_manager

    @property
    def manager(self) -> int:
        return self._manager

    def set_is_manager(self, is_manager: bool) -> None:
        self.is_manager = is_manager
        if self.manager is None:
            self._is_top_manager = True

    def __str__(self) -> str:
        return f"id = {self.employee_id}, first_name = {self.first_name}, " \
               f"manager = {self.manager}, salary = {self.salary} "
