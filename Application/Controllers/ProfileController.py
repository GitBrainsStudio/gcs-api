from fastapi import Depends

from Application.Requests.Profiles.ProfileUpdateRequest import ProfileUpdateRequest
from Application.Services.ProfileService import ProfileService
from Application.Services.TokenService import TokenService
from Startup.Services.FastApiService import FastApiService

class ProfileController : 
    _fastApiService:FastApiService = None
    _tokenService:TokenService = None
    _profileService:ProfileService = None

    def __init__(
        self,
        fastApiService:FastApiService,
        tokenService:TokenService,
        profileService:ProfileService) :
        self._fastApiService = fastApiService
        self._tokenService = tokenService
        self._profileService = profileService
        self._RegisterEndpoints()
        
    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
                    "/api/profiles/current/",
                    endpoint=self.GetCurrentProfile,
                    methods=["GET"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

        self._fastApiService._fastApi.add_api_route(
                    "/api/profiles/",
                    endpoint=self.Update,
                    methods=["PUT"],
                    dependencies=[Depends(self._tokenService.VerifyRequest)])

    async def GetCurrentProfile(self) : 
        return self._profileService.GetCurrentProfile()

    
    async def Update(self, request:ProfileUpdateRequest) : 
        return self._profileService.Update(request)