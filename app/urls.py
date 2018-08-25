from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('levels/', LevelListView.as_view(), name='level_list'),
    path('levels/<int:pk>/', LevelDetailView.as_view(), name='level_detail'),
    path('speech_to_text/', SpeechToTextView.as_view(), name='stt'),
    path('api/stt/', get_text_from_speech, name='api-stt'),
    path('api/tts/', get_speech_from_text, name='api-tts'),
]
