from django.shortcuts import render

# Create your views here.

def IndexVista(request):
    return render (request, 'index.html')
