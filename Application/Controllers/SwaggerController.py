from fastapi.openapi.docs import ( get_swagger_ui_html )

from Startup.Services.FastApiService import FastApiService

class SwaggerController : 

    _fastApiService:FastApiService = None

    def __init__(
        self, 
        fastApiService:FastApiService) :
        self._fastApiService = fastApiService
        self._RegisterEndpoints()

    def _RegisterEndpoints(self) : 
        self._fastApiService._fastApi.add_api_route(
            "/api/docs",
            endpoint=self.GetSwaggerDocumentationFromStaticFiles,
            methods=["GET"])


    async def GetSwaggerDocumentationFromStaticFiles(self) :
        return get_swagger_ui_html(
            openapi_url= self._fastApiService._fastApi.openapi_url,
            title= self._fastApiService._fastApi.title,
            oauth2_redirect_url= self._fastApiService._fastApi.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/api-documentation/swagger-ui-bundle.js",
            swagger_css_url="/static/api-documentation/swagger-ui.css")