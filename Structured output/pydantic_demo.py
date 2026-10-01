from typing import Optional, TypedDict
from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0, lt=4, default=None, description="CGPA must be between 0 and 4"
    )


new_student = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "cgpa": None,
}
student = Student(**new_student)
student_dict = student.dict()
print(
    student_dict
)  # Output: {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com', 'cgpa': None}

student_json = student.model_dump_json()
