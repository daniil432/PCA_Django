from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return HttpResponseRedirect('InputPage', {'new_user': new_user}, RequestContext(request))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'Registration.html', {'user_form': user_form})
