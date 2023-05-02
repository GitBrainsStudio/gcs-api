from Application.Controllers.AuthenticationController import AuthenticationController
from Application.Controllers.ProductController import ProductController
from Application.Controllers.ProfileController import ProfileController
from Application.Controllers.PurchaseController import PurchaseController
from Application.Controllers.SaleController import SaleController
from Application.Controllers.SwaggerController import SwaggerController
from Application.Services.AuthenticationService import AuthenticationService
from Application.Services.ConfigurationService import ConfigurationService
from Application.Services.ProductService import ProductService
from Application.Services.ProfileService import ProfileService
from Application.Services.PurchaseService import PurchaseService
from Application.Services.SaleService import SaleService
from Application.Services.TokenService import TokenService
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService
from Startup.Services.FastApiService import FastApiService
from Startup.Services.UvicornService import UvicornService

class DependenciesService :

    # Startup
    _fastApiService:FastApiService = None
    _uvicornService:UvicornService = None

    # Application
    _configurationService:ConfigurationService = None
    _authenticationService:AuthenticationService = None
    _tokenService:TokenService = None
    _profileService:ProfileService = None
    _purchaseService:PurchaseService = None
    _productService:ProductService = None
    _saleService:SaleService = None

    #Infrastucture
    _sessionService:SessionService = None

    @property
    def ConfigurationService(self) -> ConfigurationService: 
        if not self._configurationService :
            self._configurationService = ConfigurationService()
        return self._configurationService

    @property
    def AuthenticationService(self) -> AuthenticationService : 
        if not self._authenticationService :
            self._authenticationService = AuthenticationService(self.SessionService, self.TokenService)
        return self._authenticationService

    @property
    def TokenService(self) -> TokenService : 
        if not self._tokenService :
            self._tokenService = TokenService(self.ConfigurationService)
        return self._tokenService

    @property
    def ProfileService(self) -> ProfileService : 
        if not self._profileService :
            self._profileService = ProfileService(self.SessionService, self.TokenService)
        return self._profileService

    @property
    def FastApiService(self) -> FastApiService : 
        if not self._fastApiService :
            self._fastApiService = FastApiService(self.ConfigurationService)
        return self._fastApiService

    @property
    def UvicornService(self) -> UvicornService : 
        if not self._uvicornService :
            self._uvicornService = UvicornService(self.ConfigurationService, self.FastApiService)
        return self._uvicornService

    @property
    def SessionService(self) -> SessionService : 
        if not self._sessionService :
            self._sessionService = SessionService(self.ConfigurationService)
        return self._sessionService

    @property
    def PurchaseService(self) -> PurchaseService : 
        if not self._purchaseService :
            self._purchaseService = PurchaseService(self.SessionService, self.TokenService)
        return self._purchaseService

    @property
    def ProductService(self) -> ProductService : 
        if not self._productService :
            self._productService = ProductService(self.SessionService, self.TokenService)
        return self._productService

    @property
    def SaleService(self) -> SaleService : 
        if not self._saleService :
            self._saleService = SaleService(self.SessionService, self.TokenService)
        return self._saleService

    def RegisterControllers(self) :
        SwaggerController(self.FastApiService)
        AuthenticationController(self.FastApiService, self.AuthenticationService)
        ProfileController(self.FastApiService, self.TokenService, self.ProfileService)
        PurchaseController(self.FastApiService, self.TokenService, self.PurchaseService)
        ProductController(self.FastApiService, self.TokenService, self.ProductService)
        SaleController(self.FastApiService, self.TokenService, self.SaleService)