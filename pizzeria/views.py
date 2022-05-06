from django.shortcuts import render, redirect

from pizzeria.models import Pizza

# Create your views here.
def index(request):
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user)

    context = {'pizzas':pizzas}

    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, topic_id):
    pizza = Pizza.objects.get(id=topic_id)

    toppings = pizza.entry_set.order_by('-id')

    context = {'pizza':pizza,'toppings':toppings}

    return render(request, 'pizzeria/pizza.html', context)