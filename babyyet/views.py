import os

from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import BabyYet


def autoconfigure(request):
    try:
        users = User.objects.all()
        if users.count() != 0:
            raise Http404()

        username = os.environ.get('ADMIN_USERNAME')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')
        if not username or not password:
            raise Http404()

        admin = User(username=username, email=email)
        admin.set_password(password)
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()

        return HttpResponseRedirect('/')
    except:
        raise Http404()

def home(request):
    try:
        babyyet = BabyYet.objects.get(id=1)
    except BabyYet.DoesNotExist:
        babyyet = BabyYet()
        babyyet.save()
    return render(request, 'home.html', locals())


@require_http_methods(["GET", "POST"])
def supersecret(request):
    if request.method == 'POST':
        try:
            babyyet = BabyYet.objects.get(id=1)
            babyyet.baby_yet = True
            babyyet.save()
        except BabyYet.DoesNotExist:
            pass
        return HttpResponseRedirect('/')
    else:
        return render(request, 'secret.html', {})
