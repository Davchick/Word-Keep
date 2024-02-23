from .views import login

urlpatterns = [
    ('', login.as_view())
]
