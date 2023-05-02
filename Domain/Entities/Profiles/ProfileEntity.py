from sqlalchemy import Column, String

from Domain.Entities.Base import Base

class ProfileEntity(Base) : 

    __tablename__ = 'profiles'

    Id = Column('id', String, primary_key=True)
    Email = Column('email', String)
    FirstName = Column('first_name', String)
    LastName = Column('last_name', String)
    MiddleName = Column('middle_name', String)
    Password = Column('password', String)
    
    def Update(
        self,
        email:str,
        firstName:str,
        lastName:str,
        middleName:str) : 

        self.Email = email
        self.FirstName = firstName
        self.LastName = lastName
        self.MiddleName = middleName