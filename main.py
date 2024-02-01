from data import a24_movies
from recommender import suggest_categories, recommend_movies
from tree_classes import GenreNode

def display_intro():
    # ASCII Art for "Movie Finder"
    ascii_art_title = """
                      _         __ _           _           
                     (_)       / _(_)         | |          
 _ __ ___   _____   ___  ___  | |_ _ _ __   __| | ___ _ __ 
| '_ ` _ \ / _ \ \ / / |/ _ \ |  _| | '_ \ / _` |/ _ \ '__|
| | | | | | (_) \ V /| |  __/ | | | | | | | (_| |  __/ |   
|_| |_| |_|\___/ \_/ |_|\___| |_| |_|_| |_|\__,_|\___|_|                                                            
    """
    print(ascii_art_title)
    
    # App Introduction
    app_intro = """
This app helps you discover A24 studio movies based on genre and mood.
Enter keywords related to the genre of movie you're interested in,
and we'll suggest some movie moods for you to explore. If you find a mood
you like, we'll give you a list of related movie recommendations.
    """
    print(app_intro)

def main():
    display_intro()

    # Building movie tree tree
    movie_root = {}
    for genre, moods in a24_movies.items():
        genre_node = GenreNode(genre)
        for mood, movies in moods.items():
            genre_node.add_mood(mood, movies)
        movie_root[genre] = genre_node

    while True:
        # Get user input
        user_input = input("Enter a genre or mood to get movie recommendations (Horror, Comedy, Thriller, Drama), or 'quit' to exit: ").strip()
        if user_input.lower() == 'quit':
            break

        # Suggest categories based on input
        categories = suggest_categories(user_input, movie_root)
        if categories:
            print(f"Suggested categories: {', '.join(categories)}")
            selected_category = input("Select a category from the suggestions: ").strip()

            # Ensure the selected category is valid
            if selected_category.lower() in [genre.lower() for genre in movie_root]:
                genre_key = [genre for genre in movie_root if genre.lower() == selected_category.lower()][0]
                # Display moods available in the selected category
                moods = list(movie_root[genre_key].get_moods())
                print(f"Available moods in {genre_key}: {', '.join(moods)}")
                selected_mood = input("Select a mood: ").strip()
                mood_key = [mood for mood in moods if mood.lower() == selected_mood.lower()][0]

                # Recommend movies from the selected category and mood
                movies = recommend_movies(genre_key, mood_key, movie_root)
                if movies:
                    print(f"Movies in {genre_key} ({mood_key}): {', '.join(movies)}")
                else:
                    print("No movies found for the selected category and mood.")
            else:
                print("Invalid category selected.")
        else:
            print("No categories match your input. Please try again.")

        # Ask if the user wants to continue
        continue_search = input("Would you like to look for more movies? (yes/no): ").strip().lower()
        if continue_search != 'yes':
            break

if __name__ == "__main__":
    main()
