from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.template import Template, Context
import os


def hello(request):
    return HttpResponse("hello Django")


def current_datetime(request):
    now = datetime.now()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    f = open(base_dir + '/templates/current_datetime.html', 'r')
    t = Template(f.read())
    f.close()
    c = Context({'now': now})
    return HttpResponse(t.render(c))


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
