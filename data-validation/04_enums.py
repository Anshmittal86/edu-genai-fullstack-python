from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'

class User(BaseModel):
    name: str
    gender: Gender
    
user = User(name='aman',gender="male")

    