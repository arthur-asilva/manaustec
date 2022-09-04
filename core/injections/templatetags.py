from django import template
from apps.users.models import User

register = template.Library()

'''
    @register.simple_tag(name='pedidosParaSeparar')
    def pedidosParaSeparar():
        return Retiradas.objects.filter(liberado_por__isnull = True).count()

    @register.simple_tag(takes_context=True)
    def getUser(context):
        request = context['request']
        return Usuario.objects.get(id=int(request.session['appuser']))

    @register.filter(name='soma')
    def soma(value, arg):
        return value + arg
'''

@register.simple_tag(takes_context=True)
def logged_user(context, value):
    request = context['request']
    return User.objects.get(id=int(request.session['auth']))