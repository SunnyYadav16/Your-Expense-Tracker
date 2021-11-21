from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("expenses", views.index, name="expenses"),
    path("add-expense", views.add_expense, name="add-expense"),
    path("search-expenses", csrf_exempt(views.search), name="search_expenses"),
]
