import json
from heapq import heapify, heappush, heappop

games_file = open("data/games.json")
games = json.load(games_file)

genres_file = open("data/genres.json")
genres = json.load(genres_file)


# Convert genres into a hash map containing the games and there genres.
# eg -> {"Action": [Skyrim, GTA, ...], "Open-World": []}
# It is better because we only have to do this once.
def sort_by_genre():
    games_and_genres = {} 
    genre_list = genres["genres"].split(' ')
    for genre in genre_list:
        games_and_genres[genre] = []
    for game in games:
        for property in games[game]:
            if property != 'genre':
                continue
            genres_ = games[game][property].split(' ')
            for g in genres_:
                games_and_genres[g].append(game)          
    return games_and_genres

genre_sorted_games = sort_by_genre()

def display_games_by_genre(genre):
    print(f"{genre}:")
    for game in genre_sorted_games[genre]:
        print(f"   • {game}")
            
display_games_by_genre("Sandbox")

def games_in_genre(genre):
    return genre_sorted_games[genre]
    
print(games_in_genre("Sandbox"))
    
games_file.close()