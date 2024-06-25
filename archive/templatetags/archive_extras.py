from django import template

register = template.Library()


@register.filter()
def timecode(value):
    hours = int(value // 3600)
    minutes = int((value % 3600) // 60)
    seconds = int(value % 60)
    return f"{hours:01}:{minutes:02}:{seconds:02}"
