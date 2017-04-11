import logging
import urllib.request
import urllib.parse
import http.cookiejar
import json
from requests import requests
from configuration import Configuration

def logIn():
# ---! Data !---
    logging.basicConfig(filename='log',level=logging.DEBUG)
    logging.debug("Assembling the data")
    url = 'https://iu.zid.tuwien.ac.at/AuthServ.portal'
    conf = Configuration()
    usn, pw = conf.getUsernamePassword('Anil')
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
    logging.debug("parse Data " + str(values))
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
    #with requests.Session() as s:
     #   req = requests.Request('POST', url, data=data, headers=header)
     #   prepped = s.prepare_request(req)
     #   resp = s.send(prepped)
     #   print(resp.text)
    #r = requests.post(url, data=json.dumps(data), headers=header)

    with requests.Session() as session:
        logging.debug("Opened the request for the url: " + url + " with the data " + str(data))
        session.post(url, data=data)
        r = session.get("https://iu.zid.tuwien.ac.at/AuthServ.portal")
        print(r.text)
        registerCourse("j_id_43:0:j_id_8m", session)


def registerCourse(courseId, session):
    url = "https://tiss.tuwien.ac.at/education/course/examDateList.xhtml"
    values = {
        "examDateListForm" + courseId : "Anmelden",
        "examDateListForm_SUBMIT" : "1"
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')  # data should be bytes

    logging.debug("parse Data " + str(values))
    session.post(url, data=data)
    r = session.get(url)
    print(r.text)

    url2 = "https://tiss.tuwien.ac.at/education/course/register.xhtml"
    values2 = {
        "regForm:j_id_2j" : "Anmelden",
        "regForm_SUBMIT": "1"
    }
    data2 = urllib.parse.urlencode(values2)
    data2 = data2.encode('UTF-8')  # data should be bytes

    logging.debug("parse Data " + str(values2))
    session.post(url2, data=data2)
    r2 = session.get(url2)
    print(r2.text)

'''
regForm:j_id_2j:Anmelden
regForm_SUBMIT:1
javax.faces.ViewState:txSJFVo5dOyZn2VTDZIm84DdNWHA3EP29bLGxP+fcPhyZmO/
javax.faces.ClientWindow:7120
dspwid:7120
'''

def urlibTest():
    with urllib.request.urlopen('https://docs.python.org/2/howto/urllib2.html') as response:
        the_page = response.read()
        print(the_page)

logIn()