from django.shortcuts import render
from django.http import HttpResponse
from AppUsers.models import User
# Create your views here.

def users(request):
    user_list =User.objects.order_by('id')
    variables = {'user_list': user_list}
    return render(request, 'AppUsers/users.html', context=variables)

def index(request):
    return render(request, 'AppUsers/help.html', context=None)
