from fastapi import Depends

from Application.Requests.Purchases.PurchaseCreateRequest import PurchaseCreateRequest
from Application.Requests.Purchases.PurchaseUpdateRequest import PurchaseUpdateRequest
from Application.Services.PurchaseService import PurchaseService
from Application.Services.TokenService import TokenService
from Startup.Services.FastApiService import FastApiService

class PurchaseController : 
    _fastApiService:FastApiService = None
    _tokenService:TokenService = None
    _purchaseService:PurchaseService = None

    def __init__(
        self,
        fastApiService:FastApiService,
        tokenService:TokenService,
        purchaseService:PurchaseService) :
        self._fastApiService = fastApiService
        self._tokenService = tokenService
        self._purchaseService = purchaseService
        self._RegisterEndpoints()
        
    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
                    "/api/purchases/",
                    endpoint=self.GetAll,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/purchases/{id}/",
                    endpoint=self.GetById,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/purchases/",
                    endpoint=self.Create,
                    methods=["POST"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/purchases/",
                    endpoint=self.Update,
                    methods=["PUT"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/purchases/{id}/",
                    endpoint=self.Delete,
                    methods=["DELETE"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

    async def GetAll(self) : 
        return self._purchaseService.GetAll()

    async def GetById(self, id:str) : 
        return self._purchaseService.GetById(id)

    async def Create(self, request:PurchaseCreateRequest) : 
        return self._purchaseService.Create(request)

    async def Update(self, request:PurchaseUpdateRequest) : 
        return self._purchaseService.Update(request)

    async def Delete(self, id:str) : 
        return self._purchaseService.Delete(id)