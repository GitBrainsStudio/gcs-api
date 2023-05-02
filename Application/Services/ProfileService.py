from Application.Exceptions.ApplicationException import ApplicationException
from Application.Requests.Profiles.ProfileUpdateRequest import ProfileUpdateRequest
from Application.Responses.Profiles.ProfileResponse import ProfileResponse
from Application.Services.TokenService import TokenService
from Domain.Entities.Profiles.ProfileEntity import ProfileEntity
from Infrastucture.SQLAlchemy.Services.SessionServices import SessionService

class ProfileService : 

    _sessionService:SessionService
    _tokenService:TokenService

    def __init__(
        self, 
        sessionService:SessionService,
        tokenService:TokenService) :
        self._sessionService = sessionService
        self._tokenService = tokenService

    def GetCurrentProfile(self) : 
        profile:ProfileEntity = self._sessionService.DBContext.query(ProfileEntity).filter(ProfileEntity.Id == self._tokenService.Profile.Id).one()
        return ProfileResponse(profile)
    
    def Update(self, request:ProfileUpdateRequest) : 

        if (self._tokenService.Profile.Id != request.Id) : 
            raise ApplicationException('Вы можете редактировать только собственный профиль')

        profile:ProfileEntity = self._sessionService.DBContext.query(ProfileEntity).filter(ProfileEntity.Id == self._tokenService.Profile.Id).one()
        profile.Update(
            request.Email,
            request.FirstName,
            request.LastName,
            request.MiddleName)

        try : 
            self._sessionService.DBContext.commit()

        except : 
            self._sessionService.DBContext.rollback()
            raise Exception()