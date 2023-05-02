from Application.Responses.Profiles.ProfileResponse import ProfileResponse
from Domain.Entities.Profiles.ProfileEntity import ProfileEntity

class AuthenticationResponse :
    Token:str
    Profile:ProfileResponse

    def __init__(
        self,
        token:str,
        profile:ProfileResponse) :
        
        self.Token = token
        self.Profile = profile