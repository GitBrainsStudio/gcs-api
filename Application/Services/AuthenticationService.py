from Application.Requests.Authentication.AuthenticationRequest import AuthenticationRequest
from Application.Exceptions.ApplicationException import ApplicationException
from Application.Responses.Authentication.AuthenticationResponse import AuthenticationResponse
from Application.Responses.Profiles.ProfileResponse import ProfileResponse
from Application.Services.TokenService import TokenService
from Domain.Entities.Profiles.ProfileEntity import ProfileEntity
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService

class AuthenticationService : 

    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(
        self, 
        sessionService:SessionService,
        tokenService:TokenService) :
        self._sessionService = sessionService
        self._tokenService = tokenService

    def Authenticate(self, request:AuthenticationRequest) -> AuthenticationResponse: 
        
        profile:ProfileEntity = self._sessionService.DBContext.query(ProfileEntity).filter(ProfileEntity.Email == request.Email, ProfileEntity.Password == request.Password).first()
        if (profile is None) : 
            raise ApplicationException('Логин или пароль некорректен')

        return AuthenticationResponse(self._tokenService.Generate(profile), ProfileResponse(profile))