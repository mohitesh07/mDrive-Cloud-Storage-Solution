from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = AuthenticationForm()
        # Enter if the method is POST
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            # Is user is there
            if user is not None:
                login(request, user)
                messages.info(request, 'Login successfull')
                return redirect('dashboard')
            else:
                messages.warning(
                    request, 'Username or Password is incorrect.')
        # CONTEXT to render to html
        CONTEXT = {
            'form': form
        }
        # render 
        return render(request, 'accounts/login.html', CONTEXT)

def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = UserCreationForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, 'Account was created for '+user)
                return redirect('login')

        CONTEXT = {
            'form': form
        }
        return render(request, 'accounts/register.html', CONTEXT)

@login_required(login_url='login')
def LogoutUser(request):
    logout(request)
    return redirect('login')
