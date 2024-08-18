# firstapp/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("error", views.custom_404, name="custom_error"),
    path("error.html", views.custom_404, name="error"),
    path("login", views.login, name="login"),
    path("login.html", views.login, name="login"),
    path("register", views.register, name="register"),
    path("register.html", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("profile.html", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Remove or comment out handler404 if not using custom 404 view
# handler404 = views.custom_404
