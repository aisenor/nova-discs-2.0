# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StandingsSerializer


class StandingsAPIView(APIView):
    def get(self, request):
        try:
            response = requests.get('http://localhost:8000/putting_league/')
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            standings_data = process_data(data)

            serializer = StandingsSerializer(standings_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to fetch data from other endpoint: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def process_data(data):
    """
    Data is a list of dicts, each dict containing the following
        id
        date
        player (PDGA ID)
        score
    EX: [{'id': 1, 'date': '2024-01-11', 'player': 169559, 'score': 59}, ...]

    The goal of this is to sum every player's best 3 scores for every date there is
    entries and return the top 3 players for each day

    return dict with keys that are dates and values are the top 3 players
    Ex: {"2024-01-01": {"player_name": "score", ...}, ...}
    """
    processed_data = {}
    for entry in data:
        date = entry.get('date')
        player = entry.get('player')
        print(player)
        score = entry.get('score')

        # Initialize or update the player's data for the specific date
        if date not in processed_data:
            processed_data[date] = {}

        if player not in processed_data[date]:
            processed_data[date][player] = []

        # Add the score to the player's total for that date
        processed_data[date][player].append(score)

    # Create a list to store the intermediate result
    intermediate_result = []

    # Iterate over each date in the processed data
    for date, players in processed_data.items():
        # Iterate over each player on that date
        for player, scores in players.items():
            # Sort the player's scores in descending order
            sorted_scores = sorted(scores, reverse=True)

            # Take the top 3 scores
            top_3_scores = sorted_scores[:3]

            # Sum the top 3 scores for each player
            total_score = sum(top_3_scores)

            # Append the date, player, and total score to the intermediate result list
            intermediate_result.append({
                'date': date,
                'player': player,
                'total_score': total_score
            })

    # Sort the intermediate result by total score in descending order
    sorted_result = sorted(intermediate_result, key=lambda x: x['total_score'], reverse=True)

    # Take the top 3 players based on total score
    final_result = sorted_result[:3]

    print("final result")
    print(final_result)

    return final_result


