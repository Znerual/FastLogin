from configuration import Configuration

#test the configuration class:
#login credentials:
conf = Configuration()
us, pw = conf.getUsernamePassword('Laurenz')

#course entries:
print(us + ":" + pw)
id, date, place = conf.getCourseByName('GDPII')
print(str(id) + ", " + str(date) + " - " + str(place))
