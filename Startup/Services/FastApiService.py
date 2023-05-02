from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from Application.Handlers.ApplicationExceptionHandler import ApplicationExceptionHandler
from Application.Exceptions.ApplicationException import ApplicationException
from Application.Handlers.InternalExceptionHandler import InternalExceptionHandler
from Application.Services.ConfigurationService import ConfigurationService

class FastApiService : 

    _fastApi:FastAPI = None
    _configurationService:ConfigurationService = None

    def __init__(
        self, 
        configurationService:ConfigurationService) :
        self._configurationService = configurationService
        self._CreateFastAPI()
        self._ActivateApiDocumentationFilesRoute()
        self._AddExceptionHandlers()
        self._EnableCORS()

    def _CreateFastAPI(self) : 
        self._fastApi = FastAPI(
                            title=self._configurationService.FastApiTitle, 
                            version=self._configurationService.FastApiVersion, 
                            description=self._configurationService.FastApiDescription, 
                            docs_url=None, 
                            redoc_url=None,
                            openapi_url='/api/static/openapi.json')
        
    def _ActivateApiDocumentationFilesRoute(self) :
        self._fastApi.mount("/static/api-documentation", StaticFiles(directory="Static/ApiDocumentation"), name="/static/api-documentation")
       
    def _AddExceptionHandlers(self) : 
        self._fastApi.add_exception_handler(ApplicationException, ApplicationExceptionHandler().OnException)
        self._fastApi.add_exception_handler(Exception, InternalExceptionHandler().OnException)

    def _EnableCORS(self) : 
        self._fastApi.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])

    @property
    def FastApiWithCORS(self) : 
        return CORSMiddleware(
            self._fastApi,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])