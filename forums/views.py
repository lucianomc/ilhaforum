import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
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


def test_methods(request):
    context = {'message': 'Método não identificado'}

    if request.method == "GET":
        context = {'message': 'Request GET'}
    elif request.method == "POST":
        email = request.POST.get('email')
        context = {'message': 'Email %s informado!' % email}

    return render(request, 'forums/test_request.html', context)


class TestMethodsView(TemplateView):
    template_name = 'forums/test_request.html'

    def post(self, request, **kwargs):
        return render(request, 'forums/test_request.html', self.get_context_data(**kwargs))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == "GET":
            context = {'message': 'Request GET'}
        elif self.request.method == "POST":
            email = self.request.POST.get('email')
            context = {'message': 'Email %s informado!' % email}

        return context


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


class ForumJsonView(View):
    def get(self, request, **kwargs):
        dados = [
            {'name': 'Tonho da Lua'},
            {'name': 'Zé de Nanan'}
        ]

        # return JsonResponse(dados, safe=False)
        # imagem = open('caminho', 'r').read()
        # with open('camino') as arq:
        #     return


        response = HttpResponse(
            json.dumps(dados),
            content_type="application/json"
        )

        response['Content-Disposition'] = 'attachment; filename: test.json'

        return response


class FileUploadView(TemplateView):
    template_name = 'forums/upload_form.html'

    def post(self, request, **kwargs):
        breakpoint()
        return render(request,
                      self.template_name,
                      {})
