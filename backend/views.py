from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token

from .models import User

def profile(request):
    if request.method == "POST":
        data = request.POST
        user = User()
        user.login = data.get("email")
        user.password = data.get("psw")
        user.save()
    return render(request, "index.html")