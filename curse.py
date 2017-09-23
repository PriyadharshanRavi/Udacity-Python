import urllib.request
import urllib.parse

def read_text():
    
    quotes = open ("C:/Users/Priyadharshan/Downloads/Programs/Python/movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text):
  req = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + urllib.parse.urlencode([('q', text)]))
  output = req.read()
  print(output)
  req.close()\
    		
read_text()    
