from django.shortcuts import render

# Create your views here.
def index(request):
    ''' The Home Page of the Pizzeria. '''
    return render(request, 'pizzas/index.html')