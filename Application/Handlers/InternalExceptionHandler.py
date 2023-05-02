import logging
from fastapi import Request
from fastapi.responses import JSONResponse

class InternalExceptionHandler() : 
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)

    async def OnException(self, request: Request, exception: Exception):
        logging.error(str(exception))
        return JSONResponse (status_code = 500, content = {'message': 'Что-то пошло не так ☹️ (мы уже работаем над этим)' })