from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="TotalExpenses"),
    path("add-expense", views.add_expense, name="add-expense"),
]
