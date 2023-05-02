from typing import List

from Application.Requests.Sales.SaleCreateRequest import SaleCreateRequest
from Application.Requests.Sales.SaleUpdateRequest import SaleUpdateRequest
from Application.Responses.Sales.SaleResponse import SaleResponse
from Application.Services.TokenService import TokenService
from Domain.Entities.Products.ProductEntity import ProductEntity
from Domain.Entities.Sales.SaleEntity import SaleEntity
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService

class SaleService : 

    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(
        self, 
        sessionService:SessionService,
        tokenService:TokenService) :
        self._sessionService = sessionService
        self._tokenService = tokenService

    def GetAll(self) -> List[SaleResponse] : 
        return list(map(SaleResponse, self._sessionService.DBContext.query(SaleEntity).filter(SaleEntity.ProfileId == self._tokenService.Profile.Id).all()))

    def GetById(self, id:str) -> SaleResponse : 
        return SaleResponse(self._sessionService.DBContext.query(SaleEntity).filter(SaleEntity.Id == id, SaleEntity.ProfileId == self._tokenService.Profile.Id).one())

    def Create(self, request:SaleCreateRequest) : 

        product:ProductEntity = self._sessionService.DBContext.query(ProductEntity).filter(ProductEntity.Id == request.ProductId).one()

        sale:SaleEntity = SaleEntity(
            self._tokenService.Profile.Id,
            request.Price,
            request.Date)

        product.Sell(sale.Id)

        self._sessionService.DBContext.add(sale)

        try : 
            self._sessionService.DBContext.commit()

        except : 
            self._sessionService.DBContext.rollback()
            raise Exception()

    def Update(self, request:SaleUpdateRequest) : 

        sale:SaleEntity = self._sessionService.DBContext.query(SaleEntity).filter(SaleEntity.Id == request.Id, SaleEntity.ProfileId == self._tokenService.Profile.Id).one()

        if sale.Product.Id != request.ProductId : 
            sale.Product.CancelSell()
            product:ProductEntity = self._sessionService.DBContext.query(ProductEntity).filter(ProductEntity.Id == request.ProductId).one()
            product.Sell(sale.Id)

        sale.Update(
            request.Price,
            request.Date)
        
        try : 
            self._sessionService.DBContext.commit()
            
        except :
            self._sessionService.DBContext.rollback()

    def Delete(self, id:str) : 

        sale:SaleEntity = self._sessionService.DBContext.query(SaleEntity).filter(SaleEntity.Id == id, SaleEntity.ProfileId == self._tokenService.Profile.Id).one()
        sale.Product.UpdateStatus(sale.Product.Purchase.Status)
        self._sessionService.DBContext.delete(sale)

        try : 
            self._sessionService.DBContext.commit()
            
        except :
            self._sessionService.DBContext.rollback()