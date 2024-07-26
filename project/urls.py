"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from .swagger import BothHttpAndHttpsSchemaGenerator
import json

schema_view = get_schema_view(
    openapi.Info(
        title="Email-Verify API",
        default_version='v1',
        description="An API that will allow users to send sign up and the Api will verify their emails by sending them emails using the email submitted on sign up ",

        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="user@email.com"),
        license=openapi.License(name="BSD License"),
    ),

    permission_classes=[permissions.AllowAny],

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('accounts_app.urls')),
]
