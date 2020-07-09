"""sitech URL Configuration

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
from blog import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from users import views as usersViews
from rest_framework.authtoken import views as drfViews
from rest_framework.documentation import include_docs_urls

# Creates instance from DefaultRouter.
router = routers.DefaultRouter()
authRouter = routers.DefaultRouter()

# Assigning actions to routes.
router.register(r'articles', views.ArticleViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'report', views.ReactionViewSet, basename='report')
authRouter.register(r'users', usersViews.UserViewSet)

# All APIs require authentication (Token).
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include_docs_urls(title='Blog API', description='RESTful API for Blog')),
    path('api/blog/', include(router.urls)),
    path('api/auth/', include(authRouter.urls)),

    # This API will generate a Token for a user (POST username and password are reauired).
    path('api/auth/token', drfViews.obtain_auth_token, name='get_auth_toekn'),
]
