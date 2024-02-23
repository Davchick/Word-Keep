from web.http import (
    HttpResponse,
    HttpRequest,
    HTTP_STATUS_200
)
from web.core.statics import get_static
from web.core.view import View

cls
class Login(View):
    db = {
        'username': 'Seyran',
        'password': 'Nads23dsf34123sd'
    }

    async def login(self, request: HttpRequest) -> HttpResponse:
        username = request.payload.get('username')
        password = request.payload.get('password')
        if (username == self.db['username']
                and password == self.db['password']):
            return (
                HttpResponse(
                    status=HTTP_STATUS_200,
                    body=b'Login',
                )
            )

        login_page_content = await get_static('login/login.html')
        return (
            HttpResponse(
                status=HTTP_STATUS_200,
                body=login_page_content,
                headers={
                    'content-type': 'text/html'
                }
            )
        )

    async def view(self, request: HttpRequest) -> HttpResponse:
        return await self.login(request)


login = Login()
