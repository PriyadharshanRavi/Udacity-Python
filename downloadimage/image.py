import random
import urllib.request

def downloadimage(url):
	name = str(random.randrange(1,1000))
	fullname = name + ".jpg"
	urllib.request.urlretrieve(url, fullname)

downloadimage("https://static1.squarespace.com/static/55757097e4b0888fee61c30c/55888a4de4b086577bc9b655/5ac731a703ce6457531b1abd/1523004042441/Got+issues+web.jpg")
	
def downloadvideo(url):
	vname = str(random.randrange(1,1000))
	vfullname = vname + "webm"
	urllib.request.urlretrieve(url, vfullname)

downloadvideo("https://www.videvo.net/videvo_files/converted/2015_04/preview/Ocean_Waves_slow_motion_videvo.mov44965.webm")
	