from django.urls import path
from django.contrib import admin
from fuel import views

urlpatterns = [
    path('', views.home, name='home'),  # URL для главной страницы
    path('admin/', admin.site.urls),
    path('registration/', views.registration_view, name='registration'),  # URL для страницы регистрации
    path('authorisation/', views.authorisation, name='authorisation'),  # URL для страницы авторизации
    path('cart/', views.cart, name='cart'),  # URL для страницы корзины
    path('cart/<int:fuel_id>/', views.cart, name='cart'),
    path('catalog/', views.catalog, name='catalog'),  # URL для страницы каталога
    path('profile/', views.profile, name='profile'),  # URL для страницы профиля

]