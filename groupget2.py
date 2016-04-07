from urllib import urlretrieve
import urllib2
import imp,pickle,pprint
p = pprint.PrettyPrinter()

import fbconsole as fb


fb.AUTH_SCOPE = ['user_groups','read_stream']
fb.authenticate()
fb.ACCESS_TOKEN = "grab from cfg file"

gid = "grab from cfg file"


path = "/"+gid+"/feed"
params = {'fields':'actions,type'}

try:
    feed = fb.get(path,params)
except urllib2.HTTPError,err:
    print err.read()

for post in fb.iter_pages(feed):
    print post['actions'][0]['link']

output = open('feeddata.pkl', 'w')
pickle.dump(feed, output)


#p.pprint(feed)
