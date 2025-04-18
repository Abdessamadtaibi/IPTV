"""
URL configuration for IPTV_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from IPTV_api.views import *
from blog.views import *
from django.contrib.sitemaps.views import sitemap
from IPTV_api.sitemaps import *
from blog.sitemaps import *
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'static': StaticViewSitemap(),
    'plans': PlanSitemap(),
    'blog': BlogPostSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registerview,  name='register'),
    path('',homeview,  name='home'),
    path('user/',userview),
    path('login/',loginview,  name='login'),
    path('api/',include('IPTV_api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('',homeview,  name='home'),
    path('pay/plans/', plans, name='pay'),
    path('pay/plan/<slug:slug>/', pay, name='plan'),
    path('blog/', blog_index, name="blog_index"),
    path('blog/<slug:slug>/', blog_detail, name="blog_detail"),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', robots_txt, name='robots_txt'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)