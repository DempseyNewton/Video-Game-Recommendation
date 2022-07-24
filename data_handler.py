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

def ascending_price():
    heap = MinHeap(len(games))
    for game in games:
        heap.insert([game, games[game]["price"]])
    return heap

def ascending_price_genre(genre, genre_sorted_games):
    heap = MinHeap(len(genre_sorted_games[genre]))
    for game in genre_sorted_games[genre]:
        heap.insert([game, games[game]["price"]])
    return heap

def display_ascending_price(heap_list):
    for game in heap_list:
        print(f" • {game[0]} is ${game[1]}")

# Uses two indexes to find the minimum price and the maximum price in a list.
def find_prices_range(game_list, range=(0.00, 12.99)):
    middle_idx = len(game_list) // 2 
    left_idx = middle_idx
    right_idx = middle_idx
    
    while left_idx >= 0 and game_list[left_idx][1] >= range[0]:
        left_idx -= 1
    
    while right_idx < len(game_list) and game_list[right_idx][1] <= range[1]:
        right_idx += 1
    
    return (left_idx + 1, right_idx - 1)

def display_games_by_genre(genre):
    print(f"{genre}:")
    for game in genre_sorted_games[genre]:
        print(f" • {game}")
            
def games_in_genre(genre):
    return genre_sorted_games[genre]

def display_all_games():
    print("All games:")
    for game in games:
        print(f" •{game}")

games_file.close()