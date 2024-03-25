"""myproject URL Configuration

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
from django.conf.urls import url
from myapp.views import sayhello
from django.views.generic import TemplateView
from myapp.views import ViewModelPost, CreateModelPost, UpdateModelPost, DeleteModelPost
from myapp.register import signup
from django.contrib.auth import views as auth_views
from myapp.views import ViewModelProduct
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', sayhello),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^search/$', TemplateView.as_view(template_name='search.html'), name='search'),
    url(r'^signup/?$', signup, name='signup'),
    url(r'^list/$', ViewModelPost.as_view(), name= 'list'),
    url(r'^products/$', ViewModelProduct.as_view(), name= 'products'),
    url(r'^create/$', CreateModelPost.as_view(), name='create'),
    url(r'^update/(?P<id>\d+)/$', UpdateModelPost.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteModelPost.as_view(), name='delete'),
    url(r'^login/?$', auth_views.LoginView.as_view( template_name='login.html'), name='login'),
    url(r'^logout/?$', auth_views.LogoutView.as_view( template_name='home.html'), name='logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

