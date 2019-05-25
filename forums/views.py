from django.shortcuts import render
from .models import Forum

def index(request):
    forums = Forum.objects.all()
    context = { 'forums': forums }
    return render(request, 'forums/index.html', context)


def show(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    context = { 'forum': forum }
    return render(request, 'forums/show.html', context)