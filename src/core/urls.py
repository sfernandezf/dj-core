"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import re

from django.conf.urls import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import get_resolver, get_urlconf


schema_view = get_schema_view(
    openapi.Info(
        title="dj-core API",
        default_version="v1",
        description="dj-core API",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sfernandezf90@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    permission_classes=(permissions.AllowAny,),
    public=True,
)


urlpatterns = [
    # Root
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    # admin
    re_path(r"^admin/", admin.site.urls),
    # # api
    # swagger
    re_path(r"^api/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Apps
    # auth
    re_path(r"^api/auth/", include("apps.auth.urls")),
    # users
    re_path(r"^api/users/", include(("apps.users.urls", "users"), namespace="users")),

]


if settings.ENVIRONMENT == 'local':
    urlpatterns += [
        re_path(
            r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')),
            serve, kwargs=dict(document_root=settings.STATIC_ROOT)
        ),
        re_path(
            r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')),
            serve, kwargs=dict(document_root=settings.MEDIA_ROOT)
        ),
    ]
