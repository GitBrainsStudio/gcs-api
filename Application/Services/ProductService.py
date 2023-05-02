from Application.Responses.Products.ProductResponse import ProductResponse
from Application.Services.TokenService import TokenService
from Domain.Entities.Purchases.PurchaseEntity import PurchaseEntity
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService

class ProductService : 

    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(
        self, 
        sessionService:SessionService,
        tokenService:TokenService) :
        self._sessionService = sessionService
        self._tokenService = tokenService

    def GetAll(self) : 
        products = []
        purchases = self._sessionService.DBContext.query(PurchaseEntity).filter(PurchaseEntity.ProfileId == self._tokenService.Profile.Id).all()

        for purchase in purchases : 
            products.extend(purchase.Products)

        return list(map(ProductResponse, products))