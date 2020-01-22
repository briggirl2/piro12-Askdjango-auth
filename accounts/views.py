from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    request.user
    # logout: django.contrib.auth.models.AnonymousUser
    # login: django.contrib.auth.models.User

    return render(request, 'accounts/profile.html')
