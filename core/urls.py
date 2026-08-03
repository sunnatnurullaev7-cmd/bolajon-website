from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Harflar
    path('harflar/', views.letter_list, name='letter_list'),
    path('harflar/<int:pk>/', views.letter_detail, name='letter_detail'),
    
    # Raqamlar
    path('raqamlar/', views.number_list, name='number_list'),
    path('raqamlar/<int:pk>/', views.number_detail, name='number_detail'),
    
    # Hayvonlar
    path('hayvonlar/kategoriyalar/', views.animal_category_list, name='animal_category_list'),
    path('hayvonlar/', views.animal_list, name='animal_list'),
    path('hayvonlar/kategoriya/<slug:slug>/', views.animal_list, name='animal_list_by_category'),
    path('hayvonlar/<int:pk>/', views.animal_detail, name='animal_detail'),
    
    # Ranglar
    path('ranglar/', views.color_list, name='color_list'),
    
    # So'zlashuv
    path('sozlashuv/', views.conversation_list, name='conversation_list'),
    path('sozlashuv/<slug:slug>/', views.conversation_detail, name='conversation_detail'),
    
    # Mashqlar
    path('mashqlar/', views.exercise_list, name='exercise_list'),
]
