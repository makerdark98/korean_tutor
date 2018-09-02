from django.views.generic import TemplateView, ListView, CreateView
from django.http import response
from conf.settings import TTS_KEY, TTS_URL
from .models import *
from .forms import *
import requests
import json


class HomeView(TemplateView):
    template_name = 'home.html'


class LevelListView(ListView):
    template_name = 'level_list.html'
    model = Level

    def get_queryset(self):
        made_by_user = self.request.GET.get('made_by_user', False)
        queryset = super(LevelListView, self).get_queryset()
        return queryset.filter(made_by_user=made_by_user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LevelListView, self).get_context_data(object_list=object_list, **kwargs)
        context['made_by_user'] = self.request.GET.get('made_by_user', False)
        return context


class LevelDetailView(ListView):
    template_name = 'level_detail.html'
    model = Problem

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LevelDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['level'] = Level.objects.get(id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        level = self.kwargs.get('pk')
        return super(LevelDetailView, self).get_queryset().filter(level=level)


class LevelFormView(CreateView):
    model = Level
    form_class = LevelForm
    success_url = reverse_lazy('app:level_list')
    template_name = 'level_form.html'

    def get_success_url(self):
        return super(LevelFormView, self).get_success_url() + '?made_by_user=True'

    def form_valid(self, form):
        res = super(LevelFormView, self).form_valid(form)
        problems = self.request.POST.getlist('problem')
        Problem.objects.bulk_create(
            [Problem(level=self.object, title=problem) for problem in problems]
        )
        return res


def get_speech_from_text(request):
    if request.method == 'GET' and request.is_ajax():
        try:
            res = requests.get(
                url=TTS_URL,
                params={
                    'key': TTS_KEY,
                    'keyword': request.GET['keyword'],
                    'return_type': 'code'
                }
            )
            data = json.loads(res.text)

            return response.JsonResponse({'content': data['return_object']['content']})
        except Exception:
            return response.HttpResponseNotFound()
    else:
        return response.HttpResponseNotAllowed(['GET'])
