import fresh_tomatoes
import media

toy_story  = media.Movie(
	"Toy Story", 
	"A story of boy and his toys that comes to life",
	"https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
	"http://v.youku.com/v_show/id_XMTE2MDEyNDU2.html?from=s1.8-1-1.2",
	)
# print(toy_story.storyline)
# toy_story.show_trailer()

true_love = media.Movie(
	"What is True Love",
	"Storybook romances are sometimes followed by heartache, whereas true love is built on unbreakable Bible principles.",
	"https://assetsnffrgf-a.akamaihd.net/assets/m/1102012808/univ/art/1102012808_univ_lsr_lg.jpg",
	"https://tv.jw.org/#en/video/VODMovies/pub-ivtru_1_VIDEO",
	)
# print(true_love.storyline)
# true_love.show_trailer()

movies=[toy_story,true_love]
fresh_tomatoes.open_movies_page(movies)