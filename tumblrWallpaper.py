import urllib2
import urllib
import json
from pprint import pprint
api_key="3Qhylr98iTpWgR2fVPC22H64KQLWzEkqXUSWy9pHydR5mDV4kj"

def getImage(blogName):
	url="http://api.tumblr.com/v2/blog/"+blogName+".tumblr.com/posts/photo?api_key="+str(api_key)
	data=urllib2.urlopen(url)
	data=json.load(data)
	url=data["response"]["posts"][0]["photos"][0]["alt_sizes"][0]["url"]
	filename=url[url.rfind("/")+1:]	
	print filename
	urllib.urlretrieve(url,filename)
getImage("calvinhobbesdaily")
