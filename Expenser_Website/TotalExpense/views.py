from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib import messages
import json
from django.http import JsonResponse

def index(request):
    categories = Category.objects.all()
    expense = Expense.objects.filter(user=request.user)

    context = {
        'expenses': expense
    }
    return render(request, 'TotalExpense/index.html', context)

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


def search(request):
    if request.method == "POST":
        search_str = json.loads(request.body).get('searchText')

        expenses = Expense.objects.filter(amount__istartswith= search_str, user=request.user) | Expense.objects.filter(
        date__istartswith=search_str, user=request.user) | Expense.objects.filter(category__icontains= search_str,
        user=request.user) | Expense.objects.filter(description__icontains= search_str, user=request.user)

        data = expenses.values()

        return JsonResponse(list(data), safe=False)