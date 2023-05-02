from typing import List
import uuid
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from Domain.Entities.Base import Base
from Domain.Entities.Products.ProductEntity import ProductEntity
from Domain.Enums.ProductStatusEnum import ProductStatusEnum
from Domain.Enums.PurchaseStatusEnum import PurchaseStatusEnum

class PurchaseEntity(Base) : 

    __tablename__ = 'purchases'

    Id = Column('id', String, primary_key=True)
    Title = Column('title', String)
    Date = Column('date', DateTime)
    OrderNumber = Column('order_number', String)
    Status = Column('status', Integer)
    Products:List[ProductEntity] = relationship(
        "ProductEntity", 
        primaryjoin="and_(ProductEntity.PurchaseId==PurchaseEntity.Id)", 
        back_populates="Purchase",
        cascade="all, delete",
        passive_deletes=True)
    ProfileId = Column('profile_id', String)

    @hybrid_property
    def TotalAmount(self) -> int:
        totalAmount = 0
        for product in self.Products : 
            totalAmount += product.PurchasePrice
        return totalAmount

    @hybrid_property
    def ProductsCount(self) -> int:
        return len(self.Products)

    def __init__(
        self,
        profileId:str,
        title:str,
        date:str,
        orderNumber:str,
        status:PurchaseStatusEnum,
        products:List[ProductEntity]) :

        self.Id = uuid.uuid4().hex
        self.ProfileId = profileId
        self.Title = title
        self.Date = date
        self.OrderNumber = orderNumber
        self.Status = status.value
        self.Products = products

        for product in self.Products : 
            product.UpdatePurchaseId(self.Id)
            product.UpdateStatus(self.Status)

    def Update(
        self,
        title:str,
        date:str,
        orderNumber:str,
        status:PurchaseStatusEnum) : 

        self.Title = title
        self.Date = date
        self.OrderNumber = orderNumber
        self.Status = status.value

        for product in self.Products : 
            if (product.Status != ProductStatusEnum.Solded.value) :
                product.UpdateStatus(self.Status)

    def AddProduct(
        self,
        product:ProductEntity) : 

        self.Products.append(product)

    def RemoveProduct(
        self,
        product:ProductEntity) : 

        self.Products.remove(product)