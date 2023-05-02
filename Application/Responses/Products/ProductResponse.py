from Application.Responses.Purchases.PurchaseBriefResponse import PurchaseBriefResponse
from Application.Responses.Sales.SaleBriefResponse import SaleBriefResponse
from Domain.Entities.Products.ProductEntity import ProductEntity
from Domain.Enums.ProductStatusEnum import ProductStatusEnum

class ProductResponse : 

    Id:str
    Status:ProductStatusEnum
    Title:str
    PurchasePrice:int
    PurchaseBrief:PurchaseBriefResponse
    SaleBrief:SaleBriefResponse

    def __init__(
        self,
        entity:ProductEntity) :
        
        self.Id = entity.Id
        self.Status = entity.Status
        self.Title = entity.Title
        self.PurchasePrice = entity.PurchasePrice
        self.PurchaseBrief = PurchaseBriefResponse(entity.Purchase) if entity.Purchase is not None else None
        self.SaleBrief = SaleBriefResponse(entity.Sale) if entity.Sale is not None else None
        