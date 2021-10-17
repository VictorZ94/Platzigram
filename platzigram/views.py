"""Platzi views
"""
from django.http import HttpResponse, JsonResponse
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M Hrs')
    return HttpResponse(f'Oh Hi, Current server time is {now}')

def hi(request):
    numbers = request.GET['numbers']
    sorted_numbers = list(map(lambda x: int(x), numbers.split(',')))
    sorted_list = sorted(sorted_numbers)
    return JsonResponse({'status': 'OK','numbers': sorted_list})

def say_hi(request, name, age):
    if age < 12:
        message = f"Hi, {name} you're not allowed here"
    else:
        message = f"Welcome {name}"
    return HttpResponse(message)
