from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView

from accounts.forms import SignupForm


@login_required
def profile(request):
    # request.user
    # logout: django.contrib.auth.models.AnonymousUser
    # login: django.contrib.auth.models.User

    return render(request, 'accounts/profile.html')


'''
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # return redirect(settings.LOGIN_URL)
            next_url = request.GET.get('next') or 'profile'
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
'''
'''
signup = CreateView.as_view(model=User,
                            form_class=UserCreationForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')
'''


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        # return resolve_url('profile')
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()
