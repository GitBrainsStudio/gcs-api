from datetime import datetime, timedelta, timezone
from fastapi import Request
import jwt

from Application.Responses.Profiles.ProfileResponse import ProfileResponse
from Domain.Entities.Profiles.ProfileEntity import ProfileEntity
from Application.Services.ConfigurationService import ConfigurationService
from Application.Exceptions.ApplicationException import ApplicationException

class TokenService : 

    _configurationService:ConfigurationService = None
    _profile:ProfileResponse = None

    def __init__(
        self, 
        configurationService:ConfigurationService) :

        self._configurationService = configurationService

    @property
    def Profile(self) -> ProfileResponse : 
        return self._profile

    def Generate(self, profile:ProfileEntity) :

        return jwt.encode(
            {
                "exp" : datetime.now(tz=timezone.utc) + timedelta(minutes=120), "profile-info": ProfileResponse(profile).AsJson()
            }, 
            self._configurationService.JWTSecretKey,
            algorithm=self._configurationService.JWTAlgorithm)

    def VerifyRequest(self, request: Request) :

        try:
            token = request.headers.get('authorization', None)
            payload = jwt.decode(token, key=self._configurationService.JWTSecretKey, algorithms=self._configurationService.JWTAlgorithm)
            self._profile = ProfileResponse(jsonString=payload['profile-info'])

        except:
            raise ApplicationException('Запрос неавторизован', 401)
