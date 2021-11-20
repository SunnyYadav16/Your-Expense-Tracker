from . import views
from django.urls import path

urlpatterns = [
    path("expenses", views.index, name="expenses"),
    path("add-expense", views.add_expense, name="add-expense"),
]
