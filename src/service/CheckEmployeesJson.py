'''
Use pydantic to check Employee parameter types
'''

from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class CheckEmployeesJson(BaseModel):
    id: int
    first_name: str
    manager: Optional[int] = None
    salary: int

    @validator("id")
    def id_must_be_integer(cls, v) -> bool:
        try:
            return isinstance(v, int)
        except ValidationError as e:
            print("Id must be integer")
            print(e.errors())
