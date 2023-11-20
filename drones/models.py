from django.contrib.auth.models import AbstractUser
from django.db import models
import swarm_commands as swarm_commands


class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return str(self.username)


class AP(models.Model):
    ap_id = models.AutoField(primary_key=True)
    ssid = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    auth_method = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ssid)


class Swarms(models.Model):
    swarm_id = models.AutoField(primary_key=True)
    swarm_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.swarm_id)


class Drones(models.Model):
    drone_id = models.AutoField(primary_key=True)
    drone_name = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=17)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    swarm_id = models.ForeignKey(Swarms, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(Users, on_delete=models.PROTECT)

    def launch_drones(self):
        for drone in Drones.objects.filter(swarm_id=self.swarm_id):
            swarm_commands.add_drone(drone.ip_address)
        swarm_commands.launch()

    def __str__(self):
        return str(self.drone_id)
