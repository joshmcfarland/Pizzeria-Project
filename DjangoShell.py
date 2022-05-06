from cgi import print_form
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza_project.settings")

import django
django.setup()

from pizzeria.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.text)

p = Pizza.objects.get(id=1)
print(p.text)


toppings = p.topping_.all()

for t in toppings:
    print(t)
    print(t.text)
