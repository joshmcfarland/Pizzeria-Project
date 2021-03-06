from django.contrib import admin
from django.urls import path
from . import views
app_name = 'pizzeria'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>',views.pizza, name='pizza'),
    path("pizza/<int:pizza_id>/comment", views.comment, name="comment"),
    path("admin/", admin.site.urls),
]