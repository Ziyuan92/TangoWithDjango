from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    constext_dict = {'boldmessage': 'Crunchy, creamy, candy, cupcake!'}

    return render(request, 'rango/index.html', context=constext_dict)

def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")    

