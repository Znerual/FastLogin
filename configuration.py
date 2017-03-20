import xml.etree.ElementTree as ET

class Configuration:
    def __init__(self):
        self.tree = ET.parse('config.xml')
        self.root = self.tree.getroot()

    def getUsernamePassword(self,user):
        credentials = self.root.findall('login')
        for entry in credentials:
            if (entry.get('name') == user):
                return entry.find('username').text, entry.find('password').text
    def getCourseByName(self, name):
        courseList = self.root.findall('course')
        for entry in courseList:
            if (entry.get('name') == name):
                return int(entry.find('id').text), (entry.find('startDate').text), entry.find('gotPlace').text == 1
    def getCourseByDate(self, date):
        courseList = self.root.findall('course')
        for entry in courseList:
            if (entry.find('startDate') == date):
                return int(entry.find('id').text), (entry.find('startDate').text), entry.find('gotPlace').text == 1
