from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'data': range(10)
    }
    return render(request, 'holonomic/index.html', context)
