from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, GameProgress
from django.contrib import messages

@login_required
def track_game(request, game_id):
    
    game = get_object_or_404(Game, id=game_id)

    
    progress, created = GameProgress.objects.get_or_create(
        user=request.user,
        game=game
    )

    if created:
        messages.success(request, f"Started tracking progress for {game.name}.")
    else:
        messages.info(request, f"Resuming progress for {game.name}.")

    # Example: Update progress based on user input (e.g., score, level)
    if request.method == 'POST':
        new_score = int(request.POST.get('score', 0))
        new_level = int(request.POST.get('level', progress.level))
        
        progress.score += new_score
        progress.level = max(progress.level, new_level)
        progress.save()

        messages.success(request, "Your progress has been updated!")

    
    return render(request, 'track_game.html', {
        'game': game,
        'progress': progress
    })
