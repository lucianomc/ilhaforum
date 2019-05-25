from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView

from .models import Forum, Topic

@require_http_methods(['GET'])
def index(request):
    forums = Forum.objects.all()
    context = { 'forums': forums }
    return render(request, 'forums/index.html', context)


def show(request, forum_id):
        forum = Forum.objects.filter(pk=forum_id).first()
        if not forum:
                #return HttpResponseNotFound('Forum não encontrado!')
                return HttpResponse('Forum não encontrado!', status=404)

        context = { 'forum': forum }
        return render(request, 'forums/show.html', context)
    

class TopicListView(ListView):
    model = Topic