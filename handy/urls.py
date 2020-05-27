from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

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
    ),

    path('Home', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]