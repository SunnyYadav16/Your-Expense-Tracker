from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate

from django.contrib import messages
# Create your views here.

class AccountRegistration(View):
    def get(self, request):
        return render(request, 'Accounts/Register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password too short")
                    return render(request, 'Accounts/Register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Account Created Successfully")
                return render(request, 'Accounts/Register.html')

        return render(request, 'Accounts/Register.html')


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




# def AccountRegistration(request):
#
#     if request.method == 'POST':
#
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#
#             messages.success(request, "Account Created Successfully")
#             return redirect('login')
#
#     else:
#         form = CreateUserForm()
#
#     context = {'form': form}
#     return render(request, 'Accounts/Register.html', context)
