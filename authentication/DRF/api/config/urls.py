"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('health_check/', views.health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/auth/jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/auth/jwt/create/', obtain_jwt_token, name='publish_jwt_token'),
    # path('api/v1/auth/jwt/refresh/', refresh_jwt_token, name='refresh_jwt_token'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
