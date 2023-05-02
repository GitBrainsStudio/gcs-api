from typing import Optional
from pydantic import BaseModel

class ProfileUpdateRequest(BaseModel) : 

    Id:str
    Email:str
    FirstName:Optional[str]
    LastName:Optional[str]
    MiddleName:Optional[str]