from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def jahid(request):
    context = {
        'player_name' : 'jahid',
        'total_goal' : 8
    }
    return render(request, 'index.html', context)
