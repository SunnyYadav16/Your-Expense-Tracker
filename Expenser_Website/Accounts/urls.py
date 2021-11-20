from django.urls import path
from .views import *

urlpatterns = [
    # path('register', AccountRegistration.as_view(), name='registeration'),
    path('login', AccountLogin, name="login"),
    path('register', AccountRegistration, name="register"),
    path('logout', AccountLogout, name='logout')
    # path('login', AccountLogin, name="login"),
]

