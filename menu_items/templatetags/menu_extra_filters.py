from django import template

register = template.Library()


@register.filter
def set_image_src(image_url):
    return 'media/sample_menu_item.png' if not image_url else image_url
