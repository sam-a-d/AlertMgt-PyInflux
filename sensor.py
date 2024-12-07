import random

class Sensor:
    '''
        This module is responsible for producing the sensor data based on some specified criteria
    '''
    
    def __init__(self, temp=(18,30), humid=(0.3, 0.6), soilMoist=(0,1)):
        self.tags = ['high', 'mid', 'low']
        self.temp = temp
        self.humid = humid
        self.soilMoist = soilMoist
    
    def getTemp(self, *args):
        
        self.temp = args if args else self.temp
        return random.uniform(*self.temp)

    def getHumidity(self, *args):
        
        self.humid = args if args else self.humid
        return random.uniform(*self.humid)

    def getSoilMoist(self, *args):
        
        self.soilMoist = args if args else self.soilMoist
        return random.uniform(*self.soilMoist)

    def get_tag(self):

        return self.tags[random.randint(0, len(self.tags)-1)]