import urllib.request
import urllib.parse
from configuration import Configuration


logIn()

def logIn():
    url = 'https://iu.zid.tuwien.ac.at/AuthServ.portal'
    conf = Configuration()
    pw, usn = conf.getUsernamePassword('Laurenz')
    values = {'name' : usn,
              'pw' : pw,
              'totp' : '',
              'app' : '77'}

    #We have to get the cooky there. In the browser, a link to the cooky is send in the header, but the link changes dynamicly
    #so we have to find our own way to get and save the cooky
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
       the_page = response.read().decode('utf8', 'ignore') #converts the result to utf8 text
       print(the_page) #we should maybe build an HTML class with functions like getDivs() or get ElementById... to get the values
   #return the cooky or another way of authorisation


def urlibTest():
    with urllib.request.urlopen('https://docs.python.org/2/howto/urllib2.html') as response:
        the_page = response.read()
        print(the_page)
