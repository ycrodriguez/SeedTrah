from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import authenticate, login, logout

from main.forms import UserForm


class Login(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {'form': form}
        return render(request, 'custom/login.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        form = UserForm()
        context['msg'] = True
        context['form'] = form
        return render(request, 'custom/login.html', context)


class Register(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm()
        context = {'form': formRegisterUser}
        return render(request, 'custom/register.html', context)

    def post(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm(request.POST)
        if formRegisterUser.is_valid():
            formRegisterUser.save()
            return redirect('login')
        return render(request, 'custom/register.html', {'form': formRegisterUser})


class Panel(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/panel.html')


class Productos(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/productos.html')


class Prefactura(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/prefacturas.html')
