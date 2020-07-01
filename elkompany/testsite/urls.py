from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_login, name='login'),
    path('home', views.get_index, name='home'),
    path('tovar', views.get_tovar, name='tovar'),
]
