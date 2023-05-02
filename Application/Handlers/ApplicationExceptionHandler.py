from fastapi import Request
from fastapi.responses import JSONResponse

from Application.Exceptions.ApplicationException import ApplicationException

class ApplicationExceptionHandler() : 

    async def OnException(self, request: Request, exception: ApplicationException):
        return JSONResponse (status_code = exception.Code, content = {'message': exception.Message })