from Domain.Entities.Profiles.ProfileEntity import ProfileEntity

class ProfileResponse :
    Id:str
    Email:str
    FirstName:str
    LastName:str
    MiddleName:str

    def __init__(
        self,
        entity:ProfileEntity = None,
        jsonString:str = None) :
        
        if (entity is not None) : 
            self.Id = entity.Id
            self.Email = entity.Email
            self.FirstName = entity.FirstName
            self.LastName = entity.LastName
            self.MiddleName = entity.MiddleName
        
        if (jsonString is not None) : 
            self.Id = jsonString.get('Id') if jsonString.get('Id') is not None else ''
            self.Email = jsonString.get('Email') if jsonString.get('Email') is not None else ''
            self.FirstName = jsonString.get('FirstName') if jsonString.get('FirstName') is not None else ''
            self.LastName = jsonString.get('LastName') if jsonString.get('LastName') is not None else ''
            self.MiddleName = jsonString.get('MiddleName') if jsonString.get('MiddleName') is not None else ''

    def AsJson(self) -> str : 

        return {
            'Id' : self.Id,
            'Email' : self.Email,
            'FirstName' : self.FirstName,
            'LastName' : self.LastName,
            'MiddleName' : self.MiddleName
        }

    