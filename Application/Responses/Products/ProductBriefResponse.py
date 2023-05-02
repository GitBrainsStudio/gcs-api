from Domain.Entities.Products.ProductEntity import ProductEntity
from Domain.Enums.ProductStatusEnum import ProductStatusEnum

class ProductBriefResponse : 

    Id:str
    Status:ProductStatusEnum
    Title:str
    PurchasePrice:int

    def __init__(
        self,
        entity:ProductEntity) :
        
        self.Id = entity.Id
        self.Status = entity.Status
        self.Title = entity.Title
        self.PurchasePrice = entity.PurchasePrice
        