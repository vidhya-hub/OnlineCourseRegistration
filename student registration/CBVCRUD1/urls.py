"""CBVCRUD1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from CBVCRUD1 import settings
from app1 import views
from django.views.generic import TemplateView,CreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name="index.html"),name="main"),
    path('register/',views.registration.as_view(),name="register"),
    path('login',views.logincheck.as_view(),name="login"),
    path('validate/',views.validate.as_view(),name='validate'),
    path('welcome/',TemplateView.as_view(template_name="welcome.html"),name="welcome"),
    path('viewall/',views.viewall.as_view(),name="viewall"),
    path('update/<int:pk>/',views.update.as_view(),name="update"),
    path('delete/<int:pk>/',views.delete.as_view(),name="delete")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)