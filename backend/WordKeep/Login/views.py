from web.http import (
    HttpResponse,
    HttpRequest,
    HTTP_STATUS_200
)
from web.core import not_found
from web.core.statics import get_static

db = {
    'username': 'Seyran',
    'password': 'Nads23dsf34123sd'
}


async def login(request: HttpRequest) -> HttpResponse:
    username = request.payload.get('username')
    password = request.payload.get('password')
    if (username == db['username']
            and password == db['password']):
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
