from web.http import (
    HttpResponse,
    HttpRequest,
    HTTP_STATUS_200
)
from web.core.statics import get_static


async def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status=HTTP_STATUS_200,
        body=get_static('home.html'),
        headers={
            'Content-Type': 'text/html'
        }
    )
