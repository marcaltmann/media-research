from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import mail_admins
from django.shortcuts import render, redirect

from .forms import RegisterForm, RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )

            # Notify admins of new user.
            mail_admins(
                subject="New user registration",
                message=f"The user {user.username} has just registered on MMT_Py.",
            )
            # Do other stuff, e.g.:
            # Create user_files dirs (upload, download) for the user.

            return redirect('accounts:registration_complete')
        else:
            pass
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, "accounts/register.html", context)


def registration_complete(request):
    return render(request, "accounts/registration_complete.html")


@login_required()
def profile(request):
    context = {}
    return render(request, "accounts/profile.html", context)
