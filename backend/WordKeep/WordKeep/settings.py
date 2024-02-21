from web.core.statics import sp

DEBUG = True
TRACING = True
STOP_ON_EXCEPTION = False  # works only with DEBUG=False

INSTALL_APPS = [
    'Home',
    'Login'
]

STATIC_FILE_DIRS = {
    'Home': [
        sp('', 'frontend')
    ],
    'Login': [
        sp('login/', 'frontend')
    ]
}

ROOT_URLPATTERNS = [
    ('', 'Home'),
    ('login/', 'Login')
]
