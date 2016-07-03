from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.template.loader import get_template
from django.template import Template, Context
import os


def hello(request):
    return HttpResponse("hello Django")


def current_datetime(request):
    now = datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'now': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
