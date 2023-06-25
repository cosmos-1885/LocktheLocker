from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm

from locker.models import Appointment

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')

            user.set_password(form.cleaned_data['password'])
            user.save()

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')
            

            # appointment = Appointment.objects.create(user=user, locker=None)
            # appointment.save()

            return render(request, 'index.html', {'user': user})
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
@login_required
def mypage(request, user_id):
    appointment_exists = Appointment.objects.filter(user_id=user_id)
    appointment = None
    if appointment_exists:
        appointment = get_object_or_404(Appointment, pk=user_id)
    return render(request, 'mypage.html', {'appointment': appointment})