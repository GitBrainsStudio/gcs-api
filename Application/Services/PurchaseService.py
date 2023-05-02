from typing import List

from Application.Requests.Purchases.PurchaseCreateRequest import PurchaseCreateRequest
from Application.Requests.Purchases.PurchaseUpdateRequest import PurchaseUpdateRequest
from Application.Responses.Purchases.PurchaseResponse import PurchaseResponse
from Application.Exceptions.ApplicationException import ApplicationException
from Application.Services.TokenService import TokenService
from Domain.Entities.Products.ProductEntity import ProductEntity
from Domain.Entities.Purchases.PurchaseEntity import PurchaseEntity
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService

class PurchaseService : 

    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(
        self, 
        sessionService:SessionService,
        tokenService:TokenService) :
        self._sessionService = sessionService
        self._tokenService = tokenService

    def GetAll(self) -> List[PurchaseResponse] : 
        return list(map(PurchaseResponse, self._sessionService.DBContext.query(PurchaseEntity).filter(PurchaseEntity.ProfileId == self._tokenService.Profile.Id).all()))

    def GetById(self, id:str) -> PurchaseResponse : 
        return PurchaseResponse(self._sessionService.DBContext.query(PurchaseEntity).filter(PurchaseEntity.Id == id, PurchaseEntity.ProfileId == self._tokenService.Profile.Id).one())

    def Create(self, request:PurchaseCreateRequest) : 

        products:List[ProductEntity] = []
        for productCreateRequest in request.Products : 
            products.append(ProductEntity(productCreateRequest.Title, productCreateRequest.PurchasePrice))

        purchase:PurchaseEntity = PurchaseEntity(
            self._tokenService.Profile.Id,
            request.Title,
            request.Date,
            request.OrderNumber,
            request.Status,
            products
        )

        self._sessionService.DBContext.add(purchase)

        try : 
            self._sessionService.DBContext.commit()

        except : 
            self._sessionService.DBContext.rollback()
            raise Exception()

    def Update(self, request:PurchaseUpdateRequest) : 

        purchase:PurchaseEntity = self._sessionService.DBContext.query(PurchaseEntity).filter(PurchaseEntity.Id == request.Id, PurchaseEntity.ProfileId == self._tokenService.Profile.Id).one()

        for product in purchase.Products : 
            oldProduct:ProductEntity = next((e for e in request.Products if e.Id == product.Id), None)
            if oldProduct is None : 
                if product.Sale is not None :
                    raise(ApplicationException(
                        'Товар "' + product.Title + '" не доступен для удаления (по нему есть продажа)'))

                purchase.RemoveProduct(product)
                self._sessionService.DBContext.delete(product)

        for productUpdateRequest in request.Products : 
            if productUpdateRequest.Id is '': 
                purchase.AddProduct(ProductEntity(productUpdateRequest.Title, productUpdateRequest.PurchasePrice))
            else :
                product:ProductEntity = next((e for e in purchase.Products if e.Id == productUpdateRequest.Id), None)
                if product is not None : 
                    product.Update(productUpdateRequest.Title, productUpdateRequest.PurchasePrice)

        purchase.Update(
            request.Title,
            request.Date,
            request.OrderNumber,
            request.Status)

        try : 
            self._sessionService.DBContext.commit()
            
        except :
            self._sessionService.DBContext.rollback()

    def Delete(self, id:str) -> PurchaseEntity: 

        purchase:PurchaseEntity = self._sessionService.DBContext.query(PurchaseEntity).filter(PurchaseEntity.Id == id, PurchaseEntity.ProfileId == self._tokenService.Profile.Id).one()
        for product in purchase.Products : 
            if product.Sale is not None : 
                raise(ApplicationException(
                        'Закупка не доступна для удаления (по ней есть продажа)'))


        self._sessionService.DBContext.delete(purchase)

        try : 
            self._sessionService.DBContext.commit()
            
        except :
            self._sessionService.DBContext.rollback()