import os
from time import sleep
from OutageRecordsRepository import OutageRecordsRepository
from OutageReporter import OutageReporter

def ping(host):
    response = os.system("ping -c 1 " + host + " > /dev/null")

    if response == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    dbFileName = 'outages.db'
    outageRecordsRepository = OutageRecordsRepository(dbFileName)
    outageReporter = OutageReporter(outageRecordsRepository)

    while True:
        if (ping('1.1.1.1') == False):
            outageReporter.reportOutage()
        else:
            outageReporter.clearOutageStatus()

        sleep(1)
