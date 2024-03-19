from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Score

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def save_score(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        game = request.POST.get('game')
        score = request.POST.get('score')

        new_score = Score(user=user, game=game, score=score)
        new_score.save()

        return JsonResponse({'message': 'Score saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)