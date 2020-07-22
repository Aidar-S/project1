from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_login, name='login'),
    path('accounts/register/', views.MyRegisterFormView.as_view(), name='register'),
    path('home', views.get_index, name='home'),
    path('stock/tovars/', views.get_tovar, name='tovar'),
    path('stock/tovars/<int:pk>/', views.tovar_edit, name='tovar_edit'),
]
