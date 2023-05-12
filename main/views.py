from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout

from main.forms import UserForm


class Login(ListView, DetailView):
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


class Register(ListView, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/register.html')


class Panel(ListView, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/panel.html')


class Productos(ListView, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/productos.html')


class Prefactura(ListView, DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/prefacturas.html')
