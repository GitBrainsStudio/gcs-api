from datetime import date
from Domain.Entities.Purchases.PurchaseEntity import PurchaseEntity

from Domain.Enums.PurchaseStatusEnum import PurchaseStatusEnum

class PurchaseBriefResponse :
    Id:str
    Status:PurchaseStatusEnum
    Title:str
    Date:date
    OrderNumber:str
    TotalAmount:int
    ProductsCount:int

    def __init__(
        self,
        entity:PurchaseEntity) :
        
        self.Id = entity.Id
        self.Status = entity.Status
        self.Title = entity.Title
        self.Date = entity.Date
        self.OrderNumber = entity.OrderNumber
        self.TotalAmount = entity.TotalAmount
        self.ProductsCount = entity.ProductsCount