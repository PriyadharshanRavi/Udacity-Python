import fresh_tomatoes
import media

mersal = media.Movie("Mersal", "A story about Tamizhan", "http://data1.ibtimes.co.in/cache-img-900-0-photo/en/full/74172/1505882785_director-atlee-shared-vijays-upcoming-movie-mersal-teaser-poster-social-media-site-vijay-plays.jpg", "https://youtu.be/gQDo5QuZTaw")


theri = media.Movie("Theri", "A cop story", "https://moviegalleri.net/wp-content/uploads/2016/02/Atlee-Vijay-Theri%E2%80%AC-Movie-Teaser-Release-Poster.jpg", "https://youtu.be/ZK4uGLpkAKk")


vikram_vedha = media.Movie("Vikram vedha", "Grey side of a rowdy and police", "http://jfwonline.com/wp-content/uploads/2017/07/vikram-vedha.jpg", "https://youtu.be/eLucCWmf6V4")


movies = [mersal,theri,vikram_vedha]
fresh_tomatoes.open_movies_page(movies)