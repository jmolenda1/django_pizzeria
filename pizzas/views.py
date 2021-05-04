from django.shortcuts import render
from .models import Pizza, Topping, Comment
from .forms import CommentForm, PizzaForm, ToppingForm
from .forms import *

# Create your views here.
def index(request):
    ''' The Home Page of the Pizzeria. '''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    ''' Pizza List Page. '''
    pizzas = Pizza.objects.order_by('date_added')

    context = {"pizzas":pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    ''' Individual Pizzas. '''
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)



def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save() 

            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form': form, 'pizza': pizza}

    return render(request, 'pizzas/new_comment.html', context) 


