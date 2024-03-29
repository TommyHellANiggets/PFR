from django.shortcuts import render, redirect
from .models import Fuel, CartItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@login_required
def cart(request):
    return render(request, 'cart.html')

def home(request):
    fuels = Fuel.objects.all()
    return render(request, 'home.html', {'fuels': fuels})

def profile(request):
    return render(request, 'profile.html')

def catalog(request):
    return render(request, 'catalog.html')

def registration(request):
    return render(request, 'registration.html')

def authorisation(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Неверный email или пароль. Пожалуйста, попробуйте снова."

    return render(request, 'authorisation.html', {'error_message': error_message, 'user': request.user})

def registration_view(request):
    show_notification = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        agree = request.POST.get('agree')

        if password != confirm_password:
            return render(request, 'registration.html', {'show_notification': True})

        if not agree:
            return render(request, 'registration.html', {'show_notification': True})

        # Создайте пользователя
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()

        # Аутентифицируйте и войдите в систему нового пользователя
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            # Перенаправьте пользователя на нужную страницу
            return redirect('home')

    return render(request, 'registration.html', {'show_notification': show_notification})
