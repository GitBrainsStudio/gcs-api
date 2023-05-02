from pydantic import BaseModel

class AuthenticationRequest(BaseModel) : 

    Email:str
    Password:str