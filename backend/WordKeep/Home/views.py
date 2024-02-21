from web.http import (
    HttpResponse,
    HttpRequest,
    HTTP_STATUS_200
)
from web.core.statics import get_static


async def home(request: HttpRequest) -> HttpResponse:
    static_content = await get_static('home.html')

    return HttpResponse(
        status=HTTP_STATUS_200,
        body=static_content,
        headers={
            'content-type': 'text/html'
        }
    )
