from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm


def register(requ):
    if requ.method == 'POST':
        form = UserRegisterForm(requ.POST)
        if form.is_valid():
            user = form.save()
            login(requ, user)
            messages.success(requ, f'Добро пожаловать, {user.username}! Регистрация прошла успешно.')
            return redirect('shop:home')
    else:
        form = UserRegisterForm()

    return render(requ, 'users/register.html', {'form': form})


def user_logout(requ):
    logout(requ)
    messages.info(requ, 'Вы успешно вышли из системы.')
    return redirect('shop:home')