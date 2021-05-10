from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name="all"),
    path('category1/', views.category1, name="category1"),
    path('category2/', views.category2, name="category2"),
    path('category3/', views.category3, name="category3"),
    path('signIn/', views.signIn, name="signIn"),
    path('signUp/', views.signUp, name="signUp"),
    path('cart/', views.cart, name="cart")
]