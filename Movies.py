import media
import fresh_tomatoes
#To add each of my favourite movies everytime a new instance are created
premam = media.Movie("Premam",
                     "It is story of three parts of his life based on\
                     a man called Goerge and his love life",
		     "http://ecx.images-amazon.com/images/I/51flle0HSeL.jpg",
                     "https://www.youtube.com/watch?v=9wkq2PNxJys")
sachin = media.Movie("sachin",
                     "love story",
                     "https://photos.filmibeat.com/ph-big/2011/09/\
                      1317034896547175.jpg",
                     "https://www.youtube.com/watch?v=3gDvH5ajShQ")
vikram_vedha = media.Movie("Vikram Vedha",
                           "It is story based on two yound men and their\
                           struggling in their lives",
			   "https://pbs.twimg.com/media/DCcIDD2XYAAfjQ9.jpg",
			   "https://www.youtube.com/watch?v=8rnTSgcAQus")
# Here all the movie instance are added to a list
movies = [premam, sachin, vikram_vedha]
fresh_tomatoes.open_movies_page(movies)
