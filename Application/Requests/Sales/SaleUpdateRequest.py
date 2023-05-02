from pydantic import BaseModel, validator
from datetime import date
from pydantic.datetime_parse import parse_datetime

class SaleUpdateRequest(BaseModel) : 

    Id:str
    ProductId:str
    Date:date
    Price:int

    @validator('Date', pre=True)
    def ParseDate(cls, value):
        return parse_datetime(value).replace(tzinfo=None).date()