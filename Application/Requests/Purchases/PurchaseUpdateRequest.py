from typing import List
from pydantic import BaseModel, validator
from datetime import date
from pydantic.datetime_parse import parse_datetime

from Application.Requests.Products.ProductUpdateRequest import ProductUpdateRequest
from Domain.Enums.PurchaseStatusEnum import PurchaseStatusEnum

class PurchaseUpdateRequest(BaseModel) : 

    Id:str
    Title:str
    Date:date
    OrderNumber:str
    Status:PurchaseStatusEnum
    Products:List[ProductUpdateRequest]

    @validator('Date', pre=True)
    def ParseDate(cls, value):
        return parse_datetime(value).replace(tzinfo=None).date()