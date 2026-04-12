from django.urls import path
from . import views
from .views import CustomLoginView, signup_view

urlpatterns = [
    # example:
    path('',views.home,name='home'),
    path('property/', views.property_list, name='property_list'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('contact/<int:id>/', views.contact_owner, name='contact_owner'),
    path('contact/', views.contact_us, name='contact'),
    path('inquiry/', views.inquiry, name='inquiry'),
    
    path('book/', views.book_property, name='book_property_simple'),   
    path('book/<int:id>/', views.book_property, name='book_property'),
    path('location/',views.location,name='location'),
    path("login/", views.login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    
    
    
    
    
    
    
    

]