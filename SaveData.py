import json
import ast
from AlarmClass import Alarm 
 

def GetData():
    MainData = []

    # data = json.load(open('Data/AlarmsHistoryTest.json'))
    data = json.load(open('Data/GetAlarmsHistory.json'))

    for line in data['Data']:

        # for tests
        # place = line["data"]
        # date = line["alertDate"].split(" ")[0]
        # time = line["alertDate"].split(" ")[1]

        place = line["data"]
        date = line["date"]
        time = line["time"]

        MainData.append(Alarm(place,date,time))

    return MainData
    
def printAlertPerData(Data):
    for i in Data:
        print(i + " - " + str(Data[i]))

def printAlertPerDataForDrive(Data):
    for i in Data:
        print(i)

    print()
    print()

    for i in Data:
        print(str(Data[i]))