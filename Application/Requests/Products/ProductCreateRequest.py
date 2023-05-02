from pydantic import BaseModel

class ProductCreateRequest(BaseModel) : 

    Title:str
    PurchasePrice:str