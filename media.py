import webbrowser

# Class that outlines the creation of objects of type Movie
class Movie():

    # Constructor for Movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # Function that prompts the movie trailer at specified URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
