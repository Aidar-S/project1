from django.shortcuts import render, redirect
from .models import Tovar
from .forms import TovarForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound


# Create your views here.

class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = '/'

    template_name = "testsite/registration.html"

    def form_valid(self, form):
        form.save()

        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def get_login(request):
    errors = ""
    username = "not logged in"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login_user(request)
            username = form.cleaned_data['username']
            if len(form.errors) == 0:
                request.session['username'] = username
                return redirect('home')
            else:
                errors = "Логин или пароль были неправильно заполнены!"
        else:
            form = LoginForm()
    else:
        if request.session.has_key('username'):
            return redirect('home')
        else:
            form = LoginForm()

    context = {
        'Form': form,
        'error': errors,
    }

    return render(request, 'testsite/login.html', context)


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("<strong>Вы вышли!</strong>")


def get_index(request):
    context = {}
    username = request.session['username']
    tovar = Tovar.objects.all()

    context = {
        'tovars': tovar,
        'username': username,

    }

    return render(request, 'testsite/index.html', context)


def get_tovar(request):
    error = ""
    if request.method == 'POST':
        tovar = TovarForm(request.POST)
        if tovar.is_valid():
            tovar.save()
            # return redirect('home')
        else:
            error = "Ошибка, одно из полей заполнено не корректно"

    tovar = TovarForm()

    context = {
        'tovar': tovar,
        'error': error,
    }
    return render(request, 'testsite/tovar.html', context)


def tovar_edit(request, pk):
    tovar = get_object_or_404(Tovar, pk=pk)
    if request.method == "POST":
        form = TovarForm(request.POST, instance=tovar)
        if form.is_valid():
            tovar.save()
            return redirect('home')
    else:
        form = TovarForm(instance=tovar)
    return render(request, 'testsite/tovar.html', {'tovar': form})
