import json

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
            if property == 'genre':
                genres_ = games[game][property].split(' ')
                for g in genres_:
                    games_and_genres[g].append(game)
                    
    return games_and_genres
    
genre_sorted_games = sort_by_genre()

def games_in_genre(genre):
    return genre_sorted_games[genre]
    
print(games_in_genre("Action"))
    
games_file.close()