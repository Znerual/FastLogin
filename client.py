import urllib.request
import urllib.parse
import http.cookiejar
import json
from requests import requests
from configuration import Configuration

def logIn():
# ---! Data !---
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

# ---! End Of Data !---
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')  # data should be bytes
# ---! urllib attempt, (including Cookiejar) !---
   # cj = http.cookiejar.CookieJar()
#    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    #request = urllib.request.Request(url, data)
    #response = opener.open(request)
   # response.headers.add_header('Set-Cookie',
  #      'Life=ok; expires=Sat, 02-Apr-2017 18:23:03 GMT; path=/; domain=' + header['Host'] +'; HttpOnly')
   # the_page = response.read().decode('utf8', 'ignore') #converts the result to utf8 text
  #  cj.extract_cookies(response, request)
    #for cookie in cj:
        #print(cookie)
# ---! requests lib attempt (Libaray in folder requests) !---
# see http://www.pythonforbeginners.com/requests/using-requests-in-python
# and better: http://engineering.hackerearth.com/2014/08/21/python-requests-module/
    with requests.Session() as s:
        req = requests.Request('POST', url, data=data, headers=header)
        prepped = s.prepare_request(req)
        resp = s.send(prepped)
        print(resp.text)
    #r = requests.post(url, data=json.dumps(data), headers=header)





def urlibTest():
    with urllib.request.urlopen('https://docs.python.org/2/howto/urllib2.html') as response:
        the_page = response.read()
        print(the_page)

logIn()