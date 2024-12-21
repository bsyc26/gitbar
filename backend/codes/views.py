from django.shortcuts import render

def index(request):
    return render(request, 'codes/codes.html')

def code(request):
    return render(request, 'codes/code.html')

def search(request):
    return render(request, 'codes/search.html')
