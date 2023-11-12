"""
URL configuration for droneproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from drones.views import (
    home,
    user_registration,
    update_user,
    change_password,
    create_ap,
    update_ap,
    delete_ap,
    create_drone,
    update_drone,
    delete_drone,
    create_swarm,
    update_swarm,
    delete_swarm
)


urlpatterns = [
    path("", home, name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup/", user_registration, name="signup"),
    path("account/update/", update_user, name="edit_account"),
    path("account/change-password/", change_password, name="change_password"),
    path("create-ap/", create_ap, name="create_ap"),
    path("ap/<int:ap_id>/edit/", update_ap, name="edit_ap"),
    path("ap/<int:ap_id>/delete/", delete_ap, name="delete_ap"),
    path("create-drone/", create_drone, name="create_drone"),
    path("drone/<int:drone_id>/edit/", update_drone, name="edit_drone"),
    path("drone/<int:drone_id>/delete/", delete_drone, name="delete_drone"),
    path("create-swarm/", create_swarm, name="create_swarm"),
    path("swarm/<int:swarm_id>/edit/", update_swarm, name="edit_swarm"),
    path("swarm/<int:swarm_id>/delete/", delete_swarm, name="delete_swarm")
]

