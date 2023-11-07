from typing import Any
import datetime
from django.http import HttpResponse
from django.template import loader

__all__ = ['current_datetime']


def current_datetime(request: Any):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def render_html(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({}, request))
