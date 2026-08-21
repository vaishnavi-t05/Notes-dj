from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path("admin/", admin.site.urls),

    # Notes APIs
    path("api/", include("notes.urls")),

    # 2. LOGIN - JWT TOKEN
    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    # Refresh JWT Token
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]