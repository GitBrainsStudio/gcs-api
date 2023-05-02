from Application.Requests.Authentication.AuthenticationRequest import AuthenticationRequest
from Application.Services.AuthenticationService import AuthenticationService
from Startup.Services.FastApiService import FastApiService

class AuthenticationController : 
    _fastApiService:FastApiService = None
    _authenticationService:AuthenticationService = None

    def __init__(
        self,
        fastApiService:FastApiService,
        authenticationService:AuthenticationService) :
        self._fastApiService = fastApiService
        self._authenticationService = authenticationService
        self._RegisterEndpoints()
        
    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
                    "/api/authentication/",
                    endpoint=self.Authenticate,
                    methods=["POST"])

    async def Authenticate(self, request:AuthenticationRequest) : 
        return self._authenticationService.Authenticate(request)