from typing import List
from pydantic import BaseModel, validator
from datetime import date
from pydantic.datetime_parse import parse_datetime
from Application.Requests.Products.ProductCreateRequest import ProductCreateRequest

from Domain.Enums.PurchaseStatusEnum import PurchaseStatusEnum

class PurchaseCreateRequest(BaseModel) : 

    Title:str
    Date:date
    OrderNumber:str
    Status:PurchaseStatusEnum
    Products:List[ProductCreateRequest]

    @validator('Date', pre=True)
    def ParseDate(cls, value):
        return parse_datetime(value).replace(tzinfo=None).date()