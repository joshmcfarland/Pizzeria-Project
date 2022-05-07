from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pizzeria.models import Pizza, Topping, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    pizzas = Pizza.objects.filter()

    context = {'pizzas':pizzas}

    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('topping_name')

    comments = pizza.comment_set

    context = {'pizza':pizza,'toppings':toppings, 'comments':comments}

    return render(request, 'pizzeria/pizza.html', context)

@login_required
def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.owner = request.user
            comment.save()
            return redirect("pizzeria:pizza", pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza}

    return render(request, "pizzeria/comment.html", context)
