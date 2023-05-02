import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from Domain.Entities.Base import Base
from Domain.Enums.ProductStatusEnum import ProductStatusEnum
from Domain.Enums.PurchaseStatusEnum import PurchaseStatusEnum

class ProductEntity(Base) : 

    __tablename__ = 'products'

    Id = Column('id', String, primary_key=True)
    Title = Column('title', String)
    PurchasePrice = Column('price', Integer)
    Status = Column('status', Integer)
    PurchaseId = Column('purchase_id', String, ForeignKey('purchases.id', ondelete="CASCADE", onupdate="CASCADE"))
    Purchase = relationship("PurchaseEntity")
    SaleId = Column('sale_id', String, ForeignKey('sales.id'))
    Sale = relationship("SaleEntity")

    def __init__(
        self,
        title:str,
        purchasePrice:int) :

        self.Id = uuid.uuid4().hex
        self.Title = title
        self.PurchasePrice = purchasePrice

    def Sell(self, saleId:str) : 

        self.Status = ProductStatusEnum.Solded
        self.SaleId = saleId

    def UpdatePurchaseId(
        self, 
        purchaseId:str) :

        self.PurchaseId = purchaseId

    def UpdateStatus(
        self,
        purchaseStatus:PurchaseStatusEnum) : 
        
        if (purchaseStatus == PurchaseStatusEnum.InProgress) : 
            self.Status = ProductStatusEnum.InProgress

        if (purchaseStatus == PurchaseStatusEnum.Shipped) : 
            self.Status = ProductStatusEnum.Shipped

        if (purchaseStatus== PurchaseStatusEnum.Arrived) : 
            self.Status = ProductStatusEnum.Arrived

    def Update(
        self,
        title:str,
        purchasePrice:int) : 

        self.Title = title
        self.PurchasePrice = purchasePrice

    def CancelSell(
        self) : 

        self.Status = self.UpdateStatus(self.Purchase.Status)