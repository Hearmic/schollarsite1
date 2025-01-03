from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_names):
    # Проверяем, является ли group_names строкой, иначе используем список как есть
    if isinstance(group_names, str):
        group_list = group_names.split(',')  # Преобразование строки в список
    else:
        group_list = group_names  # Если это список, используем как есть

    return user.groups.filter(name__in=group_list).exists()


@register.filter(name='div')
def div(value, divisor):
    try:
        return value / divisor if divisor != 0 else 0
    except (TypeError, ValueError):
        return 0
