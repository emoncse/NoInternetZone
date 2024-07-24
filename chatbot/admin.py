from django.contrib import admin
from .models import *


# Register your models here.


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'group_name')
    search_fields = ['user', 'group_name']
    list_filter = ['user', 'group_name']


admin.site.register(UserGroup, UserGroupAdmin)


class ChattingAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'message', 'created')
    search_fields = ['name', 'group',  'created']
    list_filter = ['name', 'group',  'created']


admin.site.register(Chatting, ChattingAdmin)

