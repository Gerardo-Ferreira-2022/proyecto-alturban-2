from django.shortcuts import render

# Create your views here.

# Vista home.
def index(request):
    return render(request, 'index.html')
