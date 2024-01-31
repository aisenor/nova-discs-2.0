# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from backend.models.players import Players


class StandingsAPIView(APIView):
    def get(self, request):
        try:
            response = requests.get(f'{settings.API_URL}/putting_league/')
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            standings_data = process_data(data)
            return Response(standings_data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to fetch data from other endpoint: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def process_data(data):
    all_scores = get_all_scores(data)

    hot_rounds = hot_round_calc(all_scores)

    players_best_scores = sum_best_3_scores_per_day(all_scores)

    top_3_daily = top_3_per_day(players_best_scores)

    players_best_4_days = get_players_best_4_days(players_best_scores)

    top_5 = get_top_5_players(players_best_4_days)

    return {"top_3_daily": top_3_daily, "top_5": top_5, "hot_round": hot_rounds}


def get_all_scores(data):
    """
    Get all scores
    """
    all_scores = {}

    for entry in data:
        date = entry.get('date')
        player_id = entry.get('player')
        player = Players.objects.get(id=player_id).name

        score = entry.get('score')

        # Initialize or update the player's data for the specific date
        if date not in all_scores:
            all_scores[date] = {}

        if player not in all_scores[date]:
            all_scores[date][player] = []

        # Add the score to the player's total for that date
        all_scores[date][player].append(score)

    return all_scores


def hot_round_calc(all_scores):
    hot_rounds = {}
    for date, player_scores in all_scores.items():
        best_score = float('-inf')
        best_player = None

        for player, scores in player_scores.items():
            max_score = max(scores)
            if max_score > best_score:
                best_score = max_score
                best_player = player

        hot_rounds[date] = {best_player: best_score}

    return hot_rounds


def sum_best_3_scores_per_day(all_scores):
    daily_sums = {}

    for date, player_scores in all_scores.items():
        for player, scores in player_scores.items():
            # Sort the player's scores in descending order
            sorted_scores = sorted(scores, reverse=True)

            # Take the best 3 scores
            best_3_scores = sorted_scores[:3]

            # Sum the best 3 scores for each player on each day
            daily_sums.setdefault(date, {}).setdefault(player, 0)
            daily_sums[date][player] += sum(best_3_scores)

    return daily_sums


def top_3_per_day(daily_sums):
    # Sort the dates in descending order
    sorted_dates = sorted(daily_sums.keys(), reverse=True)

    top_3_sums_per_day = {}

    for date in sorted_dates:
        player_sums = daily_sums[date]

        # Sort the player sums in descending order
        sorted_sums = sorted(player_sums.items(), key=lambda x: x[1], reverse=True)

        # Take the top 3 sums
        top_3_sums = sorted_sums[:3]

        # Store the top 3 sums for each day
        top_3_sums_per_day[date] = top_3_sums

    return top_3_sums_per_day


def get_players_best_4_days(daily_sums):
    players_scores_all = {}

    for date, scores in daily_sums.items():
        for player, score in scores.items():
            if player not in players_scores_all:
                players_scores_all[player] = []
            players_scores_all[player].append(score)

    players_best_4_scores = {}
    for player, scores in players_scores_all.items():
        sorted_scores = sorted(scores, reverse=True)
        players_best_4_scores[player] = sorted_scores[:4]

    return players_best_4_scores


def get_top_5_players(top_4_days_per_player):
    cumulative_sums = {}

    for player, scores in top_4_days_per_player.items():
        # Calculate the cumulative sum of the best 4 days for each player
        cumulative_sum = sum(score for score in scores)
        cumulative_sums[player] = cumulative_sum

    # Take the top 5 players based on the cumulative sums
    top_5_players = sorted(cumulative_sums.items(), key=lambda x: x[1], reverse=True)[:5]

    return top_5_players
