from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError

from .models import User, Locker, Appointment

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def locker(request):
    lockers = Locker.objects.all()
    return render(request, 'appointment.html', {'lockers': lockers})


@csrf_exempt
@login_required
def appointment_create(request, locker_id):
    locker = get_object_or_404(Locker, pk=locker_id)

    # if locker.broken:
    #     return redirect('locker:appointment')
    # else:
    #     try:
    #         appointment = Appointment.objects.create(user=request.user, locker=locker)
    #         appointment.save()

    #         locker.occupied = True
    #         locker.save()

    #         return redirect('locker:appointment')
    #     except DatabaseError as DBE:
    #         return redirect('locker:appointment')

    try:
        appointment = Appointment.objects.create(user=request.user, locker=locker)
        appointment.save()

        locker.occupied = True
        locker.save()

        return redirect('locker:appointment')
    except DatabaseError as DBE:
        return redirect('locker:appointment')

@csrf_exempt
@login_required
def appointment_delete(request, user_id):
    appointment = get_object_or_404(Appointment, pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    locker_id = appointment.locker_id
    locker = get_object_or_404(Locker, pk=locker_id)

    if request.user != appointment.user:
        return redirect('locker:appointment')
    
    appointment.delete()
    locker.occupied = False
    locker.save()

    # return redirect('user:mypage', user_id)
    return render(request, 'mypage.html')

@csrf_exempt
@login_required
def manage(request):
    lockers = Locker.objects.all()
    return render(request, 'manage.html', {'lockers': lockers})

@csrf_exempt
@login_required
def appointment_initialize(request):
    appointments = Appointment.objects.all()
    for appointment in appointments:
        appointment.delete()
    
    lockers = Locker.objects.all()
    for locker in lockers:
        locker.occupied = False
        locker.broken = False
        locker.save()
    
    return render(request, 'manage.html', {'lockers': lockers})

@csrf_exempt
@login_required
def manage_broken(request, locker_id):
    locker = get_object_or_404(Locker, pk=locker_id)

    if locker.broken:
        locker.broken = False
    else:
        locker.broken = True
    locker.save()

    return redirect('locker:manage')