import data_handler

def welcome():
    print("Video Game Recommendation by Dempsey Newton")

def show_all_genres():
    choice = ''
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input("Do you want to see what genres we have? y/n: ")
    if choice == 'y':
        print("All of our genres:")
        for genre in data_handler.genres["genres"].split(' '):
            print(f" • {genre}")

welcome()

# See if user wants to see all genres.
choice = show_all_genres()

# See if user wants to sort the games by genre.
choice = ''
while choice.lower() != 'y' and choice.lower() != 'n':
    choice = input("Do you want to sort by genre? y/n: ")
sort_by_genre = choice.lower() == 'y'

# If the user does want to sort by genre, then we find out what genre.
if sort_by_genre:
    # See if user wants to see all genres.
    choice = show_all_genres()
    
    # Get what genre the user wants to sort by.
    genre = 'None'    
    while not genre in data_handler.genres["genres"].split(' '):
        genre = input("Enter genre: ")
    
choice = ''
while choice != 'y' and choice != 'n':
    choice = input("Do you wish to sort by price? y/n: ")

# If the user wants to sort by price, find out the min price and the max price.
sort_by_price = choice.lower() == 'y'
min = ''
max = ''
if sort_by_price:
    while type(min) != float:
        try:
            min = float(input("Enter min price: "))
            if min < 0:
                min = ''
                print("Min cannot be less than 0.")
        except ValueError:
            print("Enter a valid number. (Make sure there are no symbols)")
    
    while type(max) != float:
        try:
            max = float(input("Enter max price: "))
            if max <= min:
                max = ''
                print("Max cannot be equal to or less than the minimum.")
        except ValueError:
            print("Enter a valid number. (Make sure there are no symbols)")
    
# FILTERING THE GAMES AND DISPLAYING THEM.
genre_sorted_games = data_handler.sort_by_genre()
if sort_by_genre and sort_by_price:
    price_heap = data_handler.ascending_price_genre(genre, genre_sorted_games)
    price_heap.sort()
    price_range = data_handler.find_prices_range(price_heap.sorted, (min, max))
    print(f"{genre} Games (${min} - ${max}):")
    data_handler.display_ascending_price(price_heap.sorted[price_range[0]:price_range[1] + 1])
elif sort_by_genre and not sort_by_price:
    print(f"{genre} Games:")
    for game in genre_sorted_games[genre]:
        print(f" • {game}")
elif sort_by_price and not sort_by_genre:
    # Show all games in ascending price order.
    price_heap = data_handler.ascending_price()
    price_heap.sort()
    price_range = data_handler.find_prices_range(price_heap.sorted, (min, max))
    print(f"Games (${min} - ${max}):")
    data_handler.display_ascending_price(price_heap.sorted[price_range[0]:price_range[1] + 1])
else:
    choice = ''
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input("Okay, do you wish to see all games? y/n: ")
    if choice.lower() == 'y':
        data_handler.display_all_games()

choice = ''
while choice != 'y' and choice != 'n':
    choice = input("Do you wish to see information about a game? y/n: ")

if choice == 'y':
    game = ''
    while not game in data_handler.games:
        game = input("Enter games title: ")
    print(f"\nGenres: {data_handler.games[game]['genre']}")
    print(f"Price: {data_handler.games[game]['price']}")
    print(f"Release Date: {data_handler.games[game]['release date']}\n")
    print(f"Description: {data_handler.games[game]['description']}")
