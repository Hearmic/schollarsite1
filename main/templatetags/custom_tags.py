from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
    # Проверяем, является ли group_names строкой, иначе используем список как есть
    if isinstance(group_names, str):
        group_list = group_names.split(',')  # Преобразование строки в список
    else:
        group_list = group_names  # Если это список, используем как есть
    
    # Проверка на вхождение пользователя в группу
    return user.groups.filter(name__in=group_list).exists()
