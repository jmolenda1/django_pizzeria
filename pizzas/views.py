from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.
def index(request):
    ''' The Home Page of the Pizzeria. '''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    ''' Pizza List Page. '''
    pizzas = Pizza.objects.order_by('text')

    context = {"pizzas":pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    ''' Individual Pizzas. '''
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('text')
    context = {"toppings":toppings , "pizza":pizza}
    return render(request, 'pizzas/pizza.html', context)

def comments(request, pizza_id):
    if request.method == 'GET' and request.GET.get("btn1"):
        comment = request.GET.get("comment")
        print(comment)
        Comment.objects.create(post_id=pizza_id, username=request.user,text=comment,
        date_added=date.today())

    comments = Comment.objects.filter(post=pizza_id)
    post = Post.objects.get(id=pizza_id)

    context = {'post':post, 'comments':comments}
    return render(request, 'FeedApp/comments.html', context)

