class ApplicationException(Exception) : 
    Message:str = None
    Code:int = 400

    def __init__(self, message:str, code:int = 400) :
        self.Message = message
        self.Code = code
        super().__init__(message)