from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime, timedelta
from django.shortcuts import render
from django.template import RequestContext
from django.core.mail import send_mail
from .forms import ContactForm


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


def meta_data(request):
    values = request.META.items()
    # values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        # using 'initial' option doesn't bound form
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})


# Creating Context Processor
# Can be done in a separate file and registered in setting file
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


def view_1(request):
    # ...
    return render(request, 'template1.html',
                  {'message': 'I am view 1.'},
                  context_instance=RequestContext(request,
                                                  processors=[custom_proc]))


def view_2(request):
    # ...
    return render(request, 'template2.html',
                  {'message': 'I am the second view.'},
                  context_instance=RequestContext(request,
                                                  processors=[custom_proc]))
