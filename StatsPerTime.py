from AlarmClass import Alarm
from SaveData import GetData

def getAlertsPerMin():
    Data = GetData()

    AlertPerMin = {}

    for Alert in Data:
        min = Alert.getTime().split(":")[1]
        if min not in AlertPerMin:
            AlertPerMin[min] = 1
        else:
            AlertPerMin[min] = AlertPerMin[min] + 1

    AlertPerMin = dict(sorted(AlertPerMin.items(), key=lambda x:x[1], reverse=True))

    return(AlertPerMin)

def printAlertPerMin():
    Data = getAlertsPerMin()

    for i in Data:
        print(i + " - " + str(Data[i]))



def getAlertsPerHour():
    Data = GetData()

    AlertPerHour = {}

    for Alert in Data:
        hour = Alert.getTime().split(":")[0]
        if hour not in AlertPerHour:
            AlertPerHour[hour] = 1
        else:
            AlertPerHour[hour] = AlertPerHour[hour] + 1

    AlertPerHour = dict(sorted(AlertPerHour.items(), key=lambda x:x[1], reverse=True))

    return(AlertPerHour)

def printAlertPerHour():
    Data = getAlertsPerHour()

    for i in Data:
        print(i + " - " + str(Data[i]))



printAlertPerHour()