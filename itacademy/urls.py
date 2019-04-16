"""itacademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('articles/', include('articles.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from itacademy import scheme

schema_view = get_schema_view(
    scheme.api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testuser/', include('testuser.urls', namespace='testuser')),
    path('', include('main.urls', namespace='main')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('user/', include('user.urls', namespace='user')),

    re_path(
        r'^api/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=None),
        name='schema-json'
    ),
    path(
        'api/swagger/',
        # todo: выставить значение для cache. 0 отключает кеширование
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'api/redoc/',
        schema_view.with_ui('redoc', cache_timeout=None),
        name='schema-redoc'
    ),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
