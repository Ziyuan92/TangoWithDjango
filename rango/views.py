from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    constext_dict = {'boldmessage': 'Crunchy, creamy, candy, cupcake!'}

    return render(request, 'rango/index.html', context=constext_dict)

def about(request):
    context_dict = {'authorName': 'Zoe'}
    return render(request, 'rango/about.html', context=context_dict)    

