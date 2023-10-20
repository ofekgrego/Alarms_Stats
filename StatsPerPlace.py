from AlarmClass import Alarm
from SaveData import GetData
from SaveData import printAlertPerData
from SaveData import printAlertPerDataForDrive

def getAlertPerPlace():
    Data = GetData()

    AlertPerPlace = {}

    for Alert in Data:
        place = Alert.getPlace()
        if place not in AlertPerPlace:
            AlertPerPlace[place] = 1
        else:
            AlertPerPlace[place] = AlertPerPlace[place] + 1


    AlertPerPlace = dict(sorted(AlertPerPlace.items(), key=lambda x:x[1], reverse=True))

    return AlertPerPlace



def getCountOfAllPlaces():
    return(len(getAlertPerPlace()))



printAlertPerDataForDrive(getAlertPerPlace())