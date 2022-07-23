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

sort_by_price = choice.lower() == 'y'
# If the user wants to sort by price, find out the min price and the max price.
if sort_by_price:
    min = ''
    while type(min) != float:
        try:
            min = float(input("Enter min price: "))
            if min < 0:
                min = ''
                print("Min cannot be less than 0.")
        except ValueError:
            print("Enter a valid number. (Make sure there are no symbols)")
    
    max = ''
    while type(max) != float:
        try:
            max = float(input("Enter max price: "))
            if max <= min:
                max = ''
                print("Max cannot be equal to or less than the minimum.")
        except ValueError:
            print("Enter a valid number. (Make sure there are no symbols)")
    

        