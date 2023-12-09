from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menus = Menu.objects.prefetch_related('menuitem_set',  'menuitem_set__menuitemchild_set').get(name=menu_name)

    return {'menu': menus, 'current_page': context['request'].path[7:-1]}
