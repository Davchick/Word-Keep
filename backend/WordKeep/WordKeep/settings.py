from web.core.statics import sp

DEBUG = True
TRACING = True
STOP_ON_EXCEPTION = False

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 80

INSTALL_APPS = [
    'home'
]

STATIC_FILE_DIRS = {
    'home': [
        sp('', 'frontend/')
    ]
}

ROOT_URLPATTERNS = [
    ('', 'home')
]
