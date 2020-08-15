from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from handy.views import dynamic_lookup_view

from django.contrib.staticfiles.urls import static

from . import contact

from . import views

urlpatterns = [

    path('Home/', views.index, name='index'),
    
    path('contact/', contact.contact, name='contact'),

    path('admin/', admin.site.urls),

    path('register/', views.register, name='register'),

    '''
    path('login/', auth_views.LoginView.as_view(), name='login'),

    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    '''

    path('contractor/<int:ID>', dynamic_lookup_view, name='dynamic_lookup_view'),

    path('profile/', views.profile, name='profile'),

    path(
    'admin/password_reset/',auth_views.PasswordResetView.as_view(),
    name='admin_password_reset',
    ),

    path(
    'admin/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done',
    ),

    path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm',
    ),

    path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete',
    )
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns() +static(settings.STATIC_URL, document_root=settings.STATIC_URL)
