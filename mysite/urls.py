"""mysite URL Configuration

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
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings

from handy import views
from handy import contact

urlpatterns = [
    #path('admin/', admin.site.urls),
    #YOU PROBABLY WANT TO MOVE THE ADMIN URL PATTERNS HERE

    path('Home/', views.index, name='index'),
    
    path('contact/', contact.contact, name='contact'),

    path('admin/', admin.site.urls),

    path('contractor/<int:ID>', views.dynamic_lookup_view, name='dynamic_lookup_view'),
    
    path('', include("handy.urls")), 
    
    #path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
