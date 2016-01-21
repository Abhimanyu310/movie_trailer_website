import media
import fresh_tomatoes

__author__ = 'silencer310'


batman_vs_superman = media.Movie("Batman vs Superman",
                                 "http://www.chicagonow.com/matthew-milams-films-and-music/files/2015/12/batman-vs-superman.png",
                                 "https://www.youtube.com/watch?v=bEyvRQSbR5g")

dead_pool = media.Movie("Deadpool", "http://static1.squarespace.com/static/53323bb4e4b0cebc6a28ffa2/55992e15e4b040c14b12724f/55992e15e4b0eb5f8383b7b5/1436102166447/deadpool-promopic.jpg",
                       "https://www.youtube.com/watch?v=ZIM1HydF9UA")

suicide_squad = media.Movie("Suicide Squad", "https://i.ytimg.com/vi/E7N2zqCPMN0/hqdefault.jpg",
                            "https://www.youtube.com/watch?v=PLLQK9la6Go")

kungfu_3 = media.Movie("Kung Fu Panda 3", "https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg",
                       "https://www.youtube.com/watch?v=7jv24EST1rM")

captain_america = media.Movie("Captain America: Civil War", "http://t2.gstatic.com/images?q=tbn:ANd9GcQJHE0wTHT_pNRdZlnJj5IkzF49uMF3be1gfIIKw8A8z_3oHVRO",
                              "https://www.youtube.com/watch?v=1deLLCy73Qc")

conjuring_2 = media.Movie("The Conjuring 2", "http://vignette1.wikia.nocookie.net/horrormovies/images/8/86/Conjuring2.jpg/revision/latest?cb=20151019152955",
                          "https://www.youtube.com/watch?v=KyA9AtUOqRM")

movies = [batman_vs_superman, dead_pool, suicide_squad, kungfu_3, captain_america, conjuring_2]

fresh_tomatoes.open_movies_page(movies)