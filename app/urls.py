from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('levels/', LevelListView.as_view(), name='level_list'),
    path('levels/create/', LevelFormView.as_view(), name='level_create'),
    path('levels/<int:pk>/', LevelDetailView.as_view(), name='level_detail'),
    path('api/tts/', get_speech_from_text, name='api-tts'),
]
