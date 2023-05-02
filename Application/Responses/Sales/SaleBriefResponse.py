from datetime import date

from Domain.Entities.Sales.SaleEntity import SaleEntity

class SaleBriefResponse : 

    Id:str
    Price:int
    Profit:int
    Date:date

    def __init__(
        self,
        entity:SaleEntity) :
        
        self.Id = entity.Id
        self.Price = entity.Price
        self.Profit = entity.Profit
        self.Date = entity.Date
        