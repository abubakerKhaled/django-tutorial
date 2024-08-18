# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("error/", views.error, name="error"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    # Other URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error
