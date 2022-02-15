from django.urls import path
from AppUsers import views


urlpatterns = [
    path('', views.index, name='index'),
    path("users", views.users, name="users"),
]