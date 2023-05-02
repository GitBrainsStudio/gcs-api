import json
import os

class ConfigurationService : 

    _fastApiConfigurationData:any = None
    _uvicornConfigurationData:any = None
    _dataBaseConfigurationData:any = None
    _jwtConfigurationData:any = None

    def __init__(self) :
        self._ReadFastApiConfigurationFile()
        self._ReadUvicornConfigurationFile()
        self._ReadDataBaseConfigurationFile()
        self._ReadJWTConfigurationFile()

    @property
    def FastApiTitle(self) : 
        return self._fastApiConfigurationData["title"]

    @property
    def FastApiVersion(self) : 
        return self._fastApiConfigurationData["version"]

    @property
    def FastApiDescription(self) : 
        return self._fastApiConfigurationData["description"]

    @property
    def UvicornHost(self) : 
        return self._uvicornConfigurationData["host"]

    @property
    def UvicornPort(self) : 
        return self._uvicornConfigurationData["port"]
        
    @property
    def SqliteConnectionString(self) : 
        return self._dataBaseConfigurationData["sqlite-connection-string"]
    
    @property
    def JWTSecretKey(self) : 
        return self._jwtConfigurationData["jwt-secret-key"]

    @property
    def JWTAlgorithm(self) : 
        return self._jwtConfigurationData["jwt-algorithm"]

    def _ReadFastApiConfigurationFile(self) : 
         with open(os.path.join(os.getcwd(), 'Application', 'Configurations', 'FastApi.config.json'), 'r', encoding="utf-8") as f :
            self._fastApiConfigurationData = json.load(f)

    def _ReadUvicornConfigurationFile(self) : 
         with open(os.path.join(os.getcwd(), 'Application', 'Configurations', 'Uvicorn.config.json'), 'r', encoding="utf-8") as f :
            self._uvicornConfigurationData = json.load(f)

    def _ReadDataBaseConfigurationFile(self) : 
         with open(os.path.join(os.getcwd(), 'Application', 'Configurations', 'DataBase.config.json'), 'r', encoding="utf-8") as f :
            self._dataBaseConfigurationData = json.load(f)

    def _ReadJWTConfigurationFile(self) : 
         with open(os.path.join(os.getcwd(), 'Application', 'Configurations', 'JWT.config.json'), 'r', encoding="utf-8") as f :
            self._jwtConfigurationData = json.load(f)