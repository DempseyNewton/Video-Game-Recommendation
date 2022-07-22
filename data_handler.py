import json
from min_heap import MinHeap

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

def ascending_price_genre(genre):
    heap = MinHeap(len(genre_sorted_games[genre]))
    for game in genre_sorted_games[genre]:
        heap.insert([game, games[game]["price"]])
    return heap

def display_ascending_price(heap):
    for game in heap.sorted:
        print(f"  • {game[0]} is ${game[1]}")

def display_games_by_genre(genre):
    print(f"{genre}:")
    for game in genre_sorted_games[genre]:
        print(f"   • {game}")
            
def games_in_genre(genre):
    return genre_sorted_games[genre]

genre_sorted_games = sort_by_genre()
price_heap = ascending_price_genre("Action")
price_heap.sort()
print("Action Games (Ascedning Price):")
display_ascending_price(price_heap)   
        
games_file.close()