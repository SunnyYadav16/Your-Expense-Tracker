from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import login,logout,authenticate

from django.contrib import messages
# Create your views here.

# class AccountRegistration(View):
#     def get(self, request):
#         return render(request, 'Accounts/Register.html')
#
# class AccountLogin(View):
#     def get(self, request):
#         return render(request, 'Accounts/Login.html')

def AccountRegistration(request):

    form = CreateUserForm(request.POST)

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()

        user.profile.username = form.cleaned_data.get('username')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.password1 = form.cleaned_data.get('password1')
        user.profile.password2 = form.cleaned_data.get('password2')

        messages.success(request, "Account Created Successfully")
        return redirect('login')

    # else:
    #     return redirect('register')

    context = {'form': form}
    return render(request, 'Accounts/Register.html', context)

def AccountLogin(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'TotalExpense/home.html')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    return render(request, 'Accounts/Login.html')


def AccountLogout(request):
    logout(request)
    return redirect('login')