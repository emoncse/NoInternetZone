import os

from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import upper
from django.shortcuts import render

from chatGPT import settings
from chatGPT.settings import BASE_DIR
from .models import UserGroup

from chatbot.models import Chatting


@login_required
def chat_page(request):
    return render(request, 'chat.html')

@login_required
def chat(request):
    if request.method == 'POST':
        print(request.POST)
        message = request.POST.get('message', None)
        print("Messages --- >>>> ", message)
        print("Imageeeeeeeeeeeee ---->>>> ", request.POST.get('files'), type(request.POST.get('files')))
        user_group = UserGroup.objects.filter(user=request.user).first()
        if message != '' or message is not None:
            existing = Chatting.objects.filter(name=request.user, group=user_group.group_name).order_by('created').first()
            print(existing)
            if existing is None:
                data = Chatting.objects.create(name=request.user, message=message, image=request.POST['files'], group=user_group.group_name)
                print('Data Saved.')
            elif  existing != message:
                data = Chatting.objects.create(name=request.user, message=message, image=request.POST['files'],
                                               group=user_group.group_name)
                print('Data Saved.')

        all_grouped_user = UserGroup.objects.filter(group_name=user_group.group_name)
        list_of_group_user = [x.user for x in all_grouped_user]
        print(list_of_group_user)
        queryset = Chatting.objects.filter(name__in=list_of_group_user).order_by('-created')
        response_text = queryset.filter(group=user_group.group_name)
        return render(request, "chat.html", context={'response_text': response_text, 'group_name': user_group.group_name})
    else:
        user_group = UserGroup.objects.filter(user=request.user).first()
        all_grouped_user = UserGroup.objects.filter(group_name=user_group.group_name)
        list_of_group_user = [x.user for x in all_grouped_user]
        print(list_of_group_user)
        queryset = Chatting.objects.filter(name__in=list_of_group_user).order_by('-created')
        response_text = queryset.filter(group=user_group.group_name)
        return render(request, "chat.html", context={'response_text': response_text, 'group_name': user_group.group_name})
