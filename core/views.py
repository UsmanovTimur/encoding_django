from typing import Any
import datetime
from django.http import HttpResponse

__all__ = ['current_datetime']


def current_datetime(request: Any):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
