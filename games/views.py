from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import GameRecord
import json

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        game_type = data.get('game_type')
        game_settings = json.loads(data.get('game_settings'))
        final_score = data.get('final_score')

     #some input validation here?  
        
        if not game_type or not isinstance(game_type, str):
            return JsonResponse({'error': 'Invalid game_type'}, status=400)

        if not game_settings or not isinstance(game_settings, dict):
            return JsonResponse({'error': 'Invalid game_settings'}, status=400)

        if not final_score or not isinstance(final_score, int):
            return JsonResponse({'error': 'Invalid final_score'}, status=400) 

        GameRecord.objects.create(
            user=user,
            game_type=game_type,
            game_settings=game_settings,
            final_score=final_score,
        )

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
def leaderboard(request, game_type):
    top_scores = GameRecord.objects.filter(game_type=game_type).order_by('-final_score')[:10]
    top_scores_list = list(top_scores.values('user__username', 'final_score'))

    return JsonResponse(top_scores_list, safe=False)