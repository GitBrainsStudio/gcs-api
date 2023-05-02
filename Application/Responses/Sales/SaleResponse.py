from datetime import date

from Application.Responses.Products.ProductBriefResponse import ProductBriefResponse
from Domain.Entities.Sales.SaleEntity import SaleEntity

class SaleResponse : 

    Id:str
    Price:int
    Profit:int
    Date:date
    ProductBrief:ProductBriefResponse

    def __init__(
        self,
        entity:SaleEntity) :
        
        self.Id = entity.Id
        self.Price = entity.Price
        self.Profit = entity.Profit
        self.Date = entity.Date
        self.ProductBrief = ProductBriefResponse(entity.Product)
        