import pytest

from src.entity.Employee import Employee
from src.service.EmployeeService import EmployeeService


def test_find_team_members():
    employee_dict = {
        1: Employee(1, "Jean", 0, 100000),
        2: Employee(2, "Kevin", 1, 100000),
        3: Employee(3, "KB", 1, 100000),
        4: Employee(4, "Athena", 2, 100000),
        5: Employee(5, "Selena", 3, 100000)
    }

    service = EmployeeService()
    assert service.find_team_members(employee_dict, 1)
