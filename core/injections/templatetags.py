from django import template

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