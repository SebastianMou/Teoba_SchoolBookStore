from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    
]