from django.shortcuts import render, redirect
from .models import Tovar
from .forms import TovarForm, LoginForm


# Create your views here.

def get_login(request):
    if request.method == "GET":
        form = LoginForm()


    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login_user(request)
            if len(form.errors) == 0:
                return redirect('home')

    context = {
        'Form': form
    }

    return render(request, 'testsite/login.html', context)


def get_index(request):
    context = {}

    tovar = Tovar.objects.all()

    context['tovars'] = tovar

    return render(request, 'testsite/index.html', context)


def get_tovar(request):
    error = ""
    if request.method == 'POST':
        tovar = TovarForm(request.POST)
        if tovar.is_valid():
            tovar.save()
            # return redirect('home')
        else:
            error = "Ошибка"

    tovar = TovarForm()

    context = {
        'tovar': tovar,
        'error': error,
    }
    return render(request, 'testsite/tovar.html', context)
