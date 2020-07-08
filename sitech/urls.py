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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views
from users import views as usersViews
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
userRouter = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'categories', views.CategoryViewSet)
userRouter.register(r'users', usersViews.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include_docs_urls(title='Blog API', description='RESTful API for Blog')),
    path('api/blog/', include(router.urls)),
    path('api/auth/', include(userRouter.urls)),
]
