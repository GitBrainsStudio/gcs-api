import uvicorn

from Application.Services.ConfigurationService import ConfigurationService
from Startup.Services.FastApiService import FastApiService

class UvicornService : 

    _configurationService:ConfigurationService = None
    _fastApiService:FastApiService = None

    def __init__(
        self, 
        configurationService:ConfigurationService,
        fastApiService:FastApiService) :

        self._configurationService = configurationService
        self._fastApiService = fastApiService

    def RunApi(self) : 
        uvicorn.run(
            self._fastApiService.FastApiWithCORS, 
            host=self._configurationService.UvicornHost, 
            port=self._configurationService.UvicornPort
        )