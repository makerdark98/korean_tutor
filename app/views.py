from django.views.generic import TemplateView, ListView
from django.http import response
from conf.settings import TTS_KEY, TTS_URL
from .models import *
import requests, json


class HomeView(TemplateView):
    template_name = 'home.html'


class LevelListView(ListView):
    template_name = 'level_list.html'
    model = Level


class LevelDetailView(ListView):
    template_name = 'level_detail.html'
    model = Problem

    def get_queryset(self):
        level = self.kwargs.get('pk')
        return super(LevelDetailView, self).get_queryset().filter(level=level)


class SpeechToTextView(TemplateView):
    template_name = 'speech_to_text.html'


def get_text_from_speech(request):

    return


def get_speech_from_text(request):
    # if request.method == 'GET' and request.is_ajax():
    if request.method == 'GET':
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
