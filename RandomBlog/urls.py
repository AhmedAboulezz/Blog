"""RandomBlog URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from blog.views import BlogListView , BlogDetailView,BlogDeleteView , BlogUpdateView , BlogCreateView , SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',BlogListView,name='home'),
    url(r'^deletemyblogs/(?P<pk>\d+)/$',BlogDeleteView.as_view(),name='delete'),
    url(r'^myblogs/(?P<id>\d+)/$',BlogDetailView,name='detail'),
    url(r'^updatemyblogs/(?P<pk>\d+)/$',BlogUpdateView.as_view(),name='update'),
    url(r'^createblog/$',BlogCreateView.as_view(),name='create'),
    url(r'^signup/$',SignUp.as_view(),name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]