import uuid
from datetime import date
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.ext.hybrid import hybrid_property

from Domain.Entities.Base import Base
from Domain.Entities.Products.ProductEntity import ProductEntity

class SaleEntity(Base) : 

    __tablename__ = 'sales'

    Id = Column('id', String, primary_key=True)
    Price = Column('price', Integer)
    Date = Column('date', DateTime)
    Product: Mapped['ProductEntity'] = relationship()
    ProfileId = Column('profile_id', String)

    @hybrid_property
    def Profit(self) -> int:
        return self.Price - self.Product.PurchasePrice

    def __init__(
        self,
        profileId:str,
        price:int,
        date:date) :

        self.Id = uuid.uuid4().hex
        self.ProfileId = profileId
        self.Price = price
        self.Date = date

    def Update(
        self,
        price:int,
        date:date) : 

        self.Price = price
        self.Date = date
        self.Product.Sell(self.Id)

    def CalculateProfit(
        self,
        price:str,
        purchasePrice:str) -> int: 

        return price - purchasePrice