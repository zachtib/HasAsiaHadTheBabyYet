from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import BabyYet


def autoconfigure(request):
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


def home(request):
    try:
        babyyet = BabyYet.objects.get(id=1)
    except BabyYet.DoesNotExist:
        babyyet = BabyYet()
        babyyet.save()
    return render(request, 'home.html', locals())
