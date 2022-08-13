"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Pre_HomePage.as_view(),name='pre_home'),
    url(r'^home/$',views.HomePage.as_view(),name='home'),
    url(r'^home/accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^home/accounts/',include('django.contrib.auth.urls')),
    url(r'^home/test/',views.TestPage.as_view(),name='test'),
    url(r'^home/thanks/',views.ThanksPage.as_view(),name='thanks'),
    url(r'^home/posts/',include('posts.urls',namespace='posts')),
    url(r'^home/groups/',include('groups.urls',namespace='groups')),
    url(r'^about/',views.AboutPage.as_view(),name='about'),
]
