from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib import messages

def index(request):
    categories = Category.objects.all()
    return render(request, 'TotalExpense/index.html')

def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'TotalExpense/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            return render(request, 'TotalExpense/add_expense.html', context)
        description = request.POST['desc']
        date = request.POST['expense_date']
        category = request.POST['category']

        Expense.objects.create(user=request.user, amount=amount, date=date, category=category, description=description)

    return redirect('expenses')