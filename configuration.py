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
