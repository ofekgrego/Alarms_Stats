from AlarmClass import Alarm
from SaveData import GetData
from SaveData import printAlertPerData
from SaveData import printAlertPerDataForDrive

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

def printAlertPerData(Data):
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


def getAlertsPerMinSpecific(ArrayOfPlaces):
    Data = GetData()

    AlertPerMin = {}

    for Alert in Data:
        if Alert.getPlace() in ArrayOfPlaces:
            min = Alert.getTime().split(":")[1]
            if min not in AlertPerMin:
                AlertPerMin[min] = 1
            else:
                AlertPerMin[min] = AlertPerMin[min] + 1

    AlertPerMin = dict(sorted(AlertPerMin.items(), key=lambda x:x[1], reverse=True))

    return(AlertPerMin)


def getAlertsPerHourSpecific(ArrayOfPlaces):
    Data = GetData()

    AlertPerHour = {}

    for Alert in Data:
        if Alert.getPlace() in ArrayOfPlaces:
            hour = Alert.getTime().split(":")[0]
            if hour not in AlertPerHour:
                AlertPerHour[hour] = 1
            else:
                AlertPerHour[hour] = AlertPerHour[hour] + 1

    AlertPerHour = dict(sorted(AlertPerHour.items(), key=lambda x:x[1], reverse=True))

    return(AlertPerHour)



Places = ["ראשון לציון - מערב","חולון","ראשון לציון - מזרח","נס ציונה","באר יעקב","רחובות","רמת גן - מערב","בת-ים","תל אביב - דרום העיר ויפו","תל אביב - מרכז העיר","אזור","פארק תעשיות פלמחים","תל אביב - מזרח","בית דגן","גבעתיים","תל אביב - עבר הירקו","בני ברק","פתח תקווה","רמת גן - מזרח"]
Places = ["ראשון לציון - מערב","חולון","ראשון לציון - מזרח","נס ציונה","באר יעקב","רחובות"]
# Data = getAlertsPerHourSpecific(Places)


printAlertPerDataForDrive(getAlertsPerHourSpecific(Places))
print()
print()
printAlertPerDataForDrive(getAlertsPerMinSpecific(Places))
