from django.urls import path
from .views import index, html_main_page, multipage, sign_in, register, catalog, delivery, contacts, reviews  # импортируем index для указания пути

urlpatterns = [
    path('', index),  # когда будет запускаться вьюшка index
    # path('home', index),
    path('main_page', html_main_page, name='home'),
    path('multi_page/<int:page_id>', multipage),
    path('login', sign_in, name='login'),
    path('register', register, name='register'),
    path('catalog', catalog, name='catalog'),
    path('delivery', delivery, name='delivery'),
    path('contacts', contacts, name='contacts'),
    path('reviews', reviews, name='reviews'),
]
