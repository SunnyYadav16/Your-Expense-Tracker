from django.urls import path
from .views import *

urlpatterns = [
    path('register', AccountRegistration.as_view(), name='register'),
    path('login', AccountLogin, name="login"),
    path('logout', AccountLogout, name='logout'),
    # path('register', AccountRegistration, name="register"),
]

