import random

class Sensor:
    '''
        This module is responsible for producing the sensor data based on some specified criteria
    '''
    
    def __init__(self, temp=(18,30), humid=(0.05, 0.8), soilSaturatoin=(0,1), water_level=(0,5), \
                 flow_velocity=(0,5), rainfall=(0,1000), windSpeed=(0,150)):
        
        # self.tags = ['high', 'mid', 'low']
        self.water_level = water_level
        self.flow_velocity = flow_velocity
        self.soilSaturatoin = soilSaturatoin
        self.rainfall = rainfall
        self.windSpeed = windSpeed

        self.temp = temp
        self.humid = humid
    
    def getWaterLevel(self, *args):
        
        self.water_level = args[0] if args else self.water_level
        return random.uniform(*self.water_level)
    
    def getFlowVelocity(self, *args):

        self.flow_velocity = args[0] if args else self.flow_velocity
        return random.uniform(*self.flow_velocity)

    def getSoilSaturation(self, *args):
        
        self.soilSaturatoin = args[0] if args else self.soilSaturatoin
        return random.uniform(*self.soilSaturatoin)
    
    def getCumulativeRainfall(self, *args):

        self.rainfall = args[0] if args else self.rainfall
        return random.uniform(*self.rainfall)

    def getWindSpeed(self, *args):

        self.windSpeed = args[0] if args else self.windSpeed
        return random.uniform(*self.windSpeed)

    def getTemp(self, *args):
        
        self.temp = args[0] if args else self.temp
        return random.uniform(*self.temp)

    def getHumidity(self, *args):
        
        self.humid = args[0] if args else self.humid
        return random.uniform(*self.humid)
    
    def getArea(self, *args):

        self.area = args[0] if args  else self.__getRandomArea()
        return self.area

    def getRegion(self, *args):

        self.region = args[0] if args else self.__getRandomRegion()
        return self.region
    
    def __getRandomArea(self):
        
        areas = ['Area1', 'Area2', 'Area3']
        return areas[random.randint(0, len(areas)-1)]
    
    def __getRandomRegion(self):

        regions = ['Region1', 'Region2', 'Region3']
        return regions[random.randint(0, len(regions)-1)]
