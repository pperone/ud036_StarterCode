import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story about a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

fight_club = media.Movie("Fight Club",
                         "First rule of Fight Club: don't talk about Fight Club.",
                         "https://resizing.flixster.com/ufkIoVy_j1tiHVh47VfcYcttPHY=/206x305/v1.bTsxMTM3MjQ0ODtqOzE3NTAxOzEyMDA7MTE5MTsxNTg4",
                         "https://youtu.be/SUXWAEX2jlg")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "A big group robs a casino.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://youtu.be/imm6OR605UI")

movies = [toy_story, fight_club, oceans_eleven]
fresh_tomatoes.open_movies_page(movies)
