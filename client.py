from configuration import Configuration
conf = Configuration()
us, pw = conf.getUsernamePassword('Laurenz')
print(us + ":" + pw)
