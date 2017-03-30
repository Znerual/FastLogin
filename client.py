import urllib.request
import urllib.parse
from configuration import Configuration

with urllib.request.urlopen('https://docs.python.org/2/howto/urllib2.html') as response:
    the_page = response.read()
    #print(the_page)

url = 'https://iu.zid.tuwien.ac.at/AuthServ.portal'
conf = Configuration()
pw, usn = conf.getUsernamePassword('Laurenz')
values = {'name' : usn,
          'pw' : pw,
          'totp' : '',
          'app' : '77'}
header = {
"Host":"iu.zid.tuwien.ac.at",
"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"en-US,en;q=0.5",
"Accept-Encoding":"gzip, deflate, br",
"Connection":"keep-alive",
"Upgrade-Insecure-Requests":"1"
}
data = urllib.parse.urlencode(values)
data = data.encode('UTF-8') # data should be bytes
req = urllib.request.Request(url, data)
   the_page = response.read().decode('utf8', 'ignore')
   print(the_page)
