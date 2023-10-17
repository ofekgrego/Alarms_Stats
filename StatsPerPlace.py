from AlarmClass import Alarm
from SaveData import GetData

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


def printAlertPerPlace():
    Data = getAlertPerPlace()

    for i in Data:
        print(i + " - " + str(Data[i]))


def getCountOfAllPlaces():
    return(len(getAlertPerPlace()))



printAlertPerPlace()