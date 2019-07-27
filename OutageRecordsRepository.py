import sqlite3

class OutageRecordsRepository(object):
    def __init__(self, dbFileName):
        self._dbConnection = sqlite3.connect(dbFileName)
        self._createOutagesTable()

    def createNewOutage(self, outageStartDateTime, outageEndDateTime):
        startTimestamp = OutageRecordsRepository._datetimeToString(outageStartDateTime)
        endTimestamp = OutageRecordsRepository._datetimeToString(outageEndDateTime)
        
        INSERT_OUTAGE_END_SQL = "INSERT INTO Outages(Start,End) VALUES(?,?)"

        self._executeAndCommit(INSERT_OUTAGE_END_SQL, parameters=(startTimestamp, endTimestamp))

    def updateOutageEndTimestamp(self, outageStartDateTime, newOutageEndDateTime):
        startTimestamp = OutageRecordsRepository._datetimeToString(outageStartDateTime)
        newEndTimestamp = OutageRecordsRepository._datetimeToString(newOutageEndDateTime)
        
        UPDATE_OUTAGE_END_SQL = "UPDATE Outages SET End = ? WHERE Start = ?"

        self._executeAndCommit(UPDATE_OUTAGE_END_SQL, parameters=(newEndTimestamp, startTimestamp))

    def _createOutagesTable(self):
        CREATE_OUTAGES_TABLE_SQL = """CREATE TABLE IF NOT EXISTS Outages (
                                          Start text PRIMARY KEY,
                                          End text
                                      );
                                      """
        
        self._executeAndCommit(CREATE_OUTAGES_TABLE_SQL)

    def _executeAndCommit(self, sqlCommand, parameters=None):
        cursor = self._dbConnection.cursor()

        if parameters == None:
            cursor.execute(sqlCommand)
        else:
            cursor.execute(sqlCommand, parameters)

        self._dbConnection.commit()

    @staticmethod
    def _datetimeToString(datetime):
        return datetime.strftime('%Y-%m-%d %H:%M:%S.%f')