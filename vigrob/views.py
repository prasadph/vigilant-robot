from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello Django")


def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'now': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})
