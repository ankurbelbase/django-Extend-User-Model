# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProfileForm

def home(request):
	return HttpResponse("<h3>this is home<br>")


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your profile was successfully edited.')
            return redirect('/')

    else:
        form = ProfileForm(instance=user, initial={
            'address':user.profile.address
            
            })
    return render(request, 'profile.html', {'form': form})
