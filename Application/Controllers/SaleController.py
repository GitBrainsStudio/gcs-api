from fastapi import Depends

from Application.Requests.Sales.SaleCreateRequest import SaleCreateRequest
from Application.Requests.Sales.SaleUpdateRequest import SaleUpdateRequest
from Application.Services.SaleService import SaleService
from Application.Services.TokenService import TokenService
from Startup.Services.FastApiService import FastApiService

class SaleController : 
    _fastApiService:FastApiService = None
    _tokenService:TokenService = None
    _saleService:SaleService = None

    def __init__(
        self,
        fastApiService:FastApiService,
        tokenService:TokenService,
        saleService:SaleService) :
        self._fastApiService = fastApiService
        self._tokenService = tokenService
        self._saleService = saleService
        self._RegisterEndpoints()
        
    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
                    "/api/sales/",
                    endpoint=self.GetAll,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/sales/{id}/",
                    endpoint=self.GetById,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/sales/",
                    endpoint=self.Create,
                    methods=["POST"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/sales/",
                    endpoint=self.Update,
                    methods=["PUT"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/sales/{id}/",
                    endpoint=self.Delete,
                    methods=["DELETE"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

    async def GetAll(self) : 
        return self._saleService.GetAll()

    async def GetById(self, id:str) : 
        return self._saleService.GetById(id)

    async def Create(self, request:SaleCreateRequest) : 
        return self._saleService.Create(request)

    async def Update(self, request:SaleUpdateRequest) : 
        return self._saleService.Update(request)

    async def Delete(self, id:str) : 
        return self._saleService.Delete(id)