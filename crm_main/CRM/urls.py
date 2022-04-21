# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('detail/', views.detail,name="details"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_query/', views.createquery, name="create_query"),
   
    #------------ (UPDATE URLS) ------------
    path('update_query/<str:pk>/', views.updatequery, name="update_query"),


    #------------ (UPDATE URLS) ------------
    path('delete_query/<str:pk>/', views.deletequery, name="delete_query"),

]
