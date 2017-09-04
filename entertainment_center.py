import media
import fresh_tomatoes

the_truman_show = media.Movie("The Truman Show",
                              "A man is unknowingly the star of a reality show.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMDIzODcyY2EtMmY2MC00ZWVlLTgwMzAtMjQwOWUyNmJjNTYyXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                              "https://youtu.be/loTIzXAS7v4")

fight_club = media.Movie("Fight Club",
                         "First rule of Fight Club: don't talk about Fight Club.",
                         "https://resizing.flixster.com/ufkIoVy_j1tiHVh47VfcYcttPHY=/206x305/v1.bTsxMTM3MjQ0ODtqOzE3NTAxOzEyMDA7MTE5MTsxNTg4",
                         "https://youtu.be/SUXWAEX2jlg")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "A big group robs a casino.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://youtu.be/imm6OR605UI")

lord_of_the_rings = media.Movie("Lord of the Rings",
                                "A group is tasked with the mission of destroying a ring with evil powers.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                "https://youtu.be/V75dMMIW2B4")

sideways = media.Movie("Sideways",
                       "Two friends go on a wine tour as a last single-guy bonding experience.",
                       "https://dg7kra6zb39sn.cloudfront.net/media/spotlight/page/poster-76790dda-ea18-40e9-9311-c16e27a13625.jpg",
                       "https://youtu.be/Pqbz8yojxBY")

as_good_as_it_gets = media.Movie("As Good as it Gets",
                                 "An obsessive-compulsive writer learns to love and coexist with others.",
                                 "http://www.goldenglobes.com/sites/default/files/films/as_good_as_it_gets.jpg",
                                 "https://youtu.be/rrRl2QQKkI8")

movies = [the_truman_show, fight_club, oceans_eleven, lord_of_the_rings, sideways, as_good_as_it_gets]
fresh_tomatoes.open_movies_page(movies)
