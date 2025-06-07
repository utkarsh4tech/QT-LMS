from pydantic import BaseModel, Field , EmailStr
from datetime import datetime


class Book(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=50)
    publisher: str = Field(..., min_length=2, max_length=50)
    isAvail: bool = True  # Default to available

class Member(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    mobile: str = Field(..., pattern=r"^\d{10}$")  
    email: EmailStr = Field(...)  

class Issue(BaseModel):
    bookID: int = Field(..., gt=0)
    memberID: int = Field(..., gt=0)
    issueTime: datetime = Field(default_factory=datetime.now)  
    renewCount: int = Field(0, ge=0)  

