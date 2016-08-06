import media
import fresh_tomatoes

toy_story = media.Movies("Toy Story",
                         "Woody, Bo Peep, Rex, Slinky, Mr. Potato Head, Hamm, Lenny, Slinky, Mr. Spell, and a few others are his toys. Then, as a rivalry begins between Woody and new toy Buzz. A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room",
                         "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movies("Avatar",
                      "When his brother is killed in a robbery, paraplegic Marine Jake Sully decides to take his place in a mission on the distant world of Pandora.",
                      "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg  ",
                      "https://www.youtube.com/watch?v=d1_JBMrrYw8")
school_of_rock = media.Movies("School of Rock",
                              "The main plot follows struggling rock singer and guitarist, Dewey Finn (Black), who is kicked out of his band and subsequently disguises himself as a substitute teacher at a prestigious prep school.",
                              "https://en.wikipedia.org/wiki/School_of_Rock_(musical)#/media/File:School_of_Rock_musical.jpg",
                              "https://www.youtube.com/watch?v=5afGGGsxvEA")
ratatouille = media.Movies("Ratatouille",
                           "A rat named Remy dreams of becoming a great French chef despite his family's wishes and the obvious problem of being a rat in a decidedly rodent-phobic profession.",
                           "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movies("Midnight In Paris",
                                 "In Woody Allen's film Midnight in Paris, the main character Gil, played by Owen Wilson (center) travels back in time from modern-day Paris to the city in 1920s. Allen is on the right.",
                                 "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                 "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)