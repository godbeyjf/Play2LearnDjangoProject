from django.urls import path

from games.views import MathFactsView, AnagramHuntView, save_score

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('save_score/', save_score, name='save_score'),
]