from django.contrib.auth.models import User
from django.db import models

class Chatting(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    group = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message or ''}"

class UserGroup(models.Model):
    GROUP_CHOICES = [
        ('friends', 'friends'),
        ('family', 'family'),
        ('special', 'special'),
        ('office', 'office'),
        ('school', 'school'),
        ('university', 'university'),
        ('onetoone', 'onetoone'),
        ('superuser', 'superuser'),
        ('bhaibrother', 'bhaibrother'),
        ('atik_group', 'atik_group'),
        ('mehjabin_group', 'mehjabin_group'),
        ('group1', 'group1'),
        ('group2', 'group2'),
        ('group3', 'group3'),
        ('group4', 'group4')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=500, choices=GROUP_CHOICES)

    def __str__(self):
        return f"{self.group_name} - {self.user.username}"
