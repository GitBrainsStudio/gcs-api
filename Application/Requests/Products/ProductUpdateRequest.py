from pydantic import BaseModel

class ProductUpdateRequest(BaseModel) : 

    Id:str
    Title:str
    PurchasePrice:str