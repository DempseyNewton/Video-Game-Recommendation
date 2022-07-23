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
        genre = input("Do you wish to sort by genre? Enter genre: ")
    
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
if sort_by_genre and sort_by_price:
    genre_sorted_games = data_handler.sort_by_genre()
    price_heap = data_handler.ascending_price_genre(genre, genre_sorted_games)
    price_heap.sort()
    price_range = data_handler.find_prices_range(price_heap.sorted, (min, max))
    print(f"{genre} Games (${min} - ${max}):")
    data_handler.display_ascending_price(price_heap.sorted[price_range[0]:price_range[1] + 1])  