from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chatting, UserGroup


@login_required
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message', None)
        image = request.FILES.get('files', None)
        user_group = UserGroup.objects.filter(user=request.user).first()

        if message or image:
            Chatting.objects.create(name=request.user, message=message, image=image, group=user_group.group_name)

        return JsonResponse({'status': 'success'})

    user_group = UserGroup.objects.filter(user=request.user).first()
    all_grouped_user = UserGroup.objects.filter(group_name=user_group.group_name)
    list_of_group_user = [x.user for x in all_grouped_user]
    queryset = Chatting.objects.filter(name__in=list_of_group_user).order_by('-created')
    response_text = queryset.filter(group=user_group.group_name)
    return render(request, "chat.html", context={'response_text': response_text, 'group_name': user_group.group_name})


@login_required
def chat_messages(request):
    user_group = UserGroup.objects.filter(user=request.user).first()
    all_grouped_user = UserGroup.objects.filter(group_name=user_group.group_name)
    list_of_group_user = [x.user for x in all_grouped_user]
    queryset = Chatting.objects.filter(name__in=list_of_group_user).order_by('-created')
    response_text = list(queryset.filter(group=user_group.group_name).values('name', 'message', 'image', 'created'))

    for item in response_text:
        if item['image']:
            item['image'] = request.build_absolute_uri(f"/media/{item['image']}")

    return JsonResponse(response_text, safe=False)
