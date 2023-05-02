from Startup.Services.DependenciesService import DependenciesService

_dependenciesService:DependenciesService = DependenciesService()
_dependenciesService.RegisterControllers()

_dependenciesService.UvicornService.RunApi()

def FastApi() : 
    return _dependenciesService.FastApiService.FastApiWithCORS