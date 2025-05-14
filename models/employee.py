from dataclasses import dataclass
from typing import Optional

@dataclass
class Employee:
    """
    Employee data model representing an employee record.
    """
    id: Optional[int] = None
    name: str = ""
    age: str = ""
    job: str = ""  
    email: str = ""
    gender: str = ""
    phone: str = ""
    address: str = ""
    
    def to_tuple(self):
        """Convert employee data to a tuple for database operations"""
        if self.id is None:
            return (self.name, self.age, self.job, self.email, self.gender, self.phone, self.address)
        else:
            return (self.name, self.age, self.job, self.email, self.gender, self.phone, self.address, self.id)
    
    @classmethod
    def from_tuple(cls, data_tuple):
        """Create an Employee instance from a database tuple"""
        if len(data_tuple) == 8:
            return cls(
                id=data_tuple[0],
                name=data_tuple[1],
                age=data_tuple[2],
                job=data_tuple[3],
                email=data_tuple[4],
                gender=data_tuple[5],
                phone=data_tuple[6],
                address=data_tuple[7]
            )
        return None
