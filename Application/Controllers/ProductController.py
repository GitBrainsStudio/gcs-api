from fastapi import Depends

from Application.Services.ProductService import ProductService
from Application.Services.TokenService import TokenService
from Startup.Services.FastApiService import FastApiService

class ProductController : 
    _fastApiService:FastApiService = None
    _tokenService:TokenService = None
    _productService:ProductService = None

    def __init__(
        self,
        fastApiService:FastApiService,
        tokenService:TokenService,
        productService:ProductService) :
        self._fastApiService = fastApiService
        self._tokenService = tokenService
        self._productService = productService
        self._RegisterEndpoints()
        
    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
                    "/api/products/",
                    endpoint=self.GetAll,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

    async def GetAll(self) : 
        return self._productService.GetAll()