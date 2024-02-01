# Recommendation logic for recommending movie categories and movies within a category

from tree_classes import GenreNode


def suggest_categories(input_str, movie_data):
    """
    Suggest movie categories based on the user's input string.

    :param input_str: Partial input string from the user.
    :param movie_data: The dataset containing movies categorized by genre and mood.
    :return: List of suggested categories that match the input string.
    """
    suggestions = [category for category in movie_data if input_str.lower() in category.lower()]
    return suggestions

def recommend_movies(genre, mood, movie_data):
    """
    Recommend movies from a selected genre and mood.

    :param genre: The selected movie genre.
    :param mood: The selected mood within the genre.
    :param movie_data: The dataset containing movies categorized by genre and mood.
    :return: List of movies within the selected genre and mood.
    """
    return movie_data.get(genre, GenreNode('NA')).get_mood_node(mood).get_movies()
