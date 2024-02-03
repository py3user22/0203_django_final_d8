from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),
    path('home2', views.home1),

    #203 menu urls add.
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),

    #203 header links add
    path('about/', views.about, name="about"),

    #203 book reservations add
    path('book/', views.book, name="book"),
    path('bookings/', views.bookings, name="bookings"),



]