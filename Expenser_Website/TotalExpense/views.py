from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'TotalExpense\home.html')

def add_expense(request):
    return render(request, 'TotalExpense/add_expense.html')
