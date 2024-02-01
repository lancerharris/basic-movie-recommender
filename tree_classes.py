class MovieNode:
    def __init__(self, title):
        self.title = title

class MoodNode:
    def __init__(self, mood):
        self.mood = mood
        self.movies = []  # List of MovieNode objects

    def add_movie(self, movie):
        self.movies.append(MovieNode(movie))

    def get_movies(self):
        return [movie.title for movie in self.movies]

class GenreNode:
    def __init__(self, genre):
        self.genre = genre
        self.moods = {}  # Dictionary of mood: MoodNode objects

    def add_mood(self, mood, movies):
        mood_node = MoodNode(mood)
        for movie in movies:
            mood_node.add_movie(movie)
        self.moods[mood] = mood_node
    
    def get_moods(self):
        return list(self.moods)
    
    def get_mood_node(self, mood):
        return self.moods.get(mood, MoodNode('NA'))
