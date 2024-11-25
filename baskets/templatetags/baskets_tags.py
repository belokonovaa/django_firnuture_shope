from django import template

from baskets.utils import get_user_baskets

register = template.Library()


@register.simple_tag()
def users_baskets(request):
    return get_user_baskets(request)