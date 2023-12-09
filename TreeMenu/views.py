from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Menu, MenuItemChild


# Переделать на TemplateView
class Menus(TemplateView):
    template_name = 'base.html'


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'TreeMenu/menu_detail_view.html'
    context_object_name = 'menu'


class MenuItemChildDetailView(DetailView):
    model = MenuItemChild
    template_name = 'TreeMenu/item_child_detail_view.html'
    context_object_name = 'child'
