from django.http import HttpResponse


# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('ngapp/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
