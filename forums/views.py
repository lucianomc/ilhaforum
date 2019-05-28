from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Forum, Topic


@require_http_methods(['GET'])
def index(request):
    forums = Forum.objects.all()
    context = { 'forums': forums }
    return render(request, 'forums/index.html', context)


def show(request, forum_id):
    try:
        forum = Forum.objects.get(pk=forum_id)
    except Forum.DoesNotExist:
        raise Http404("No Forum matches the given id")

    context = {'forum': forum}
    return render(request, 'forums/show.html', context)


class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic


class TopicCreateView(CreateView):
    model = Topic
    success_url = reverse_lazy('forums:topics')
    fields = ['name', 'forum']

    def get_success_url(self):
        return reverse_lazy('forums:show', kwargs={'forum_id': self.object.forum.id})



class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['name', 'forum']

    def get_success_url(self):
        return reverse_lazy('forums:topic_details', kwargs={'pk': self.get_object().id})
