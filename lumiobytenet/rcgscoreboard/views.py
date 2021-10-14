from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader

from .models import PlayerScore

# Overwrite scores or new score every time even if same username? Not sure yet

def leaderboard_redirect_view(request):

    return HttpResponseRedirect('./1/')

def leaderboard_view(request, level_selected):

    if level_selected == 3:
        allScores = PlayerScore.objects.all()
    else:
        allScores = PlayerScore.objects.filter(level = level_selected)

    return render(request, 'rcgscoreboard/leaderboard.html', {'totalScores': len(allScores), 'allScores': allScores, 'levelSelected': level_selected})

def add_score_endpoint(request):

    if request.method == "GET":

        try:
            username = request.GET['username']
            time = request.GET['seconds']
            level = request.GET['level']
        except:
            return JsonResponse({'response': "400 Bad request"}, status = 400)

        # Just adding a new one every time may not in future
        playerScoreObj = PlayerScore(username = username, time = time, level = level)
        playerScoreObj.save()

        return JsonResponse({'response': "200 OK"})
    else:
        return JsonResponse({'response': "400 Bad request"}, status = 400)

def ping_endpoint(request):

    return JsonResponse({'response': '200 OK'})