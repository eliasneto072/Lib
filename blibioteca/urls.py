from django.urls import path,re_path,include
from allauth.account.views import *

from django.conf import settings
from django.conf.urls.static import static

from . import views




urlpatterns = [
    # bliblioteca
    path('', views.homeView, name='home'),
    path('livros/', views.listlivro, name='livros'),
    path('create/', views.createlivro, name='create'),
    #path('update/<int:id>', views.updatelivro, name='update')
    
    #path('perfil/<int:id>', views.perfilView, name='perfil'),
    
    
    
    # allauth
    path("signup/", signup, name="account_signup"),
    path("login/", login, name="account_login"),
    path("logout/", logout, name="account_logout"),
    path(
        "password/change/",
        password_change,
        name="account_change_password",
    ),
    path("password/set/", password_set, name="account_set_password"),
    path("inactive/", account_inactive, name="account_inactive"),
    # E-mail
    path("email/", email, name="account_email"),
    path(
        "confirm-email/",
        email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    # password reset
    path("password/reset/", password_reset, name="account_reset_password"),
    path(
        "password/reset/done/",
        password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)