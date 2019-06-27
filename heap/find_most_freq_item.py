from collections import Counter


text =  "A December squall came in search of him and"\
		" knocked his door. Yes, It was her. She came in like a "\
		"swift stormy wind leaving no room for doubt or fear to crawl "\
		"back in. All of a sudden a hidden thought came alive. "\
		"It stole a glance at all the busyness of everyday life."\
		"It asked for words to set it free, words to wear so that it"\
		"can escape from his lips. It asked for his voice so that it "\
		"can embrace the moment and sway it with glee. But, we’ve been"\
		"so trapped in all these social mazes. Pathways that restrict"\
		"you to talk about exactly what’s going on inside you."\
		"Sly protocols that make you tweak the words. "\
		"Yes, It happened to him as well. We all have forgotten how "\

words = text.split()

counter = Counter(words)
top_ten = counter.most_common(10)

print(top_ten)