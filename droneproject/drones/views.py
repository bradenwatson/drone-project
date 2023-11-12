from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from .forms import UserRegistrationForm, UpdateUserForm, APForm, SwarmsForm, DronesForm
from .models import AP, Swarms, Drones


def home(request):
    drones = Drones.objects.all()
    swarms = Swarms.objects.all()
    aps = AP.objects.all()

    context = {
        "drones": drones,
        "swarms": swarms,
        "aps": aps
    }

    return render(request, "index.html", context)


def user_registration(request):
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    context = {"form": form}
    return render(request, "registration\\signup.html", context)


@login_required(login_url='/account/login/')
def update_user(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UpdateUserForm(instance=request.user)

    context = {"form": form}
    return render(request, "update_user.html", context)


@login_required(login_url='/account/login/')
def change_password(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SetPasswordForm(request.user)

    context = {"form": form}
    return render(request, "change_password.html", context)


@login_required(login_url='/account/login/')
def create_ap(request):
    form = APForm(request.POST or None)

    if form.is_valid():
        ap = form.save(commit=False)
        ap.updated_by = request.user
        form.save()
        return redirect("home")

    context = {
        "form": form,
        "model_name": "AP"
    }

    return render(request, "create_item.html", context)


@login_required(login_url='/account/login/')
def update_ap(request, ap_id):
    ap = AP.objects.get(ap_id=ap_id)

    if request.method == "POST":
        form = APForm(request.POST, instance=ap)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = APForm(instance=ap)

    context = {
        "form": form,
        "ap": ap
    }

    return render(request, "update_ap.html", context)


@login_required(login_url='/account/login/')
def delete_ap(request, ap_id):
    ap = AP.objects.get(ap_id=ap_id)
    ap.delete()
    return redirect("home")


@login_required(login_url='/account/login/')
def create_swarm(request):
    form = SwarmsForm(request.POST or None)

    if form.is_valid():
        swarm = form.save(commit=False)
        swarm.updated_by = request.user
        form.save()
        return redirect("home")

    context = {
        "form": form,
        "model_name": "Swarm"
    }

    return render(request, "create_item.html", context)


@login_required(login_url='/account/login/')
def update_swarm(request, swarm_id):
    swarm = Swarms.objects.get(swarm_id=swarm_id)

    if request.method == "POST":
        form = SwarmsForm(request.POST, instance=swarm)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SwarmsForm(instance=swarm)

    context = {
        "form": form,
        "swarm": swarm
    }

    return render(request, "update_swarm.html", context)


@login_required(login_url='/account/login/')
def delete_swarm(request, swarm_id):
    swarm = Swarms.objects.get(swarm_id=swarm_id)
    swarm.delete()
    return redirect("home")


@login_required(login_url='/account/login/')
def create_drone(request):
    form = DronesForm(request.POST or None)

    if form.is_valid():
        drone = form.save(commit=False)
        drone.updated_by = request.user
        form.save()
        return redirect("home")

    context = {
        "form": form,
        "model_name": "Drone"
    }

    return render(request, "create_item.html", context)


@login_required(login_url='/account/login/')
def update_drone(request, drone_id):
    drone = Drones.objects.get(drone_id=drone_id)

    if request.method == "POST":
        form = DronesForm(request.POST, instance=drone)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DronesForm(instance=drone)

    context = {
        "form": form,
        "drone": drone
    }

    return render(request, "update_drone.html", context)


@login_required(login_url='/account/login/')
def delete_drone(request, drone_id):
    drone = Drones.objects.get(drone_id=drone_id)
    drone.delete()
