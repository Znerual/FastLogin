from configuration import Configuration
conf = Configuration()
us, pw = conf.getUsernamePassword('Laurenz')
print(us + ":" + pw)
id, date, place = conf.getCourseByName('GDPII')
print(str(id) + ", " + str(date) + " - " + str(place))
