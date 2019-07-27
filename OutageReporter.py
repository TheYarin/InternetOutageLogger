from datetime import datetime

class OutageReporter(object):
    def __init__(self, outageRecordsRepository):
        self._outageDetected = False
        self._currentOutageStartTime = None
        self._outageRecordsRepository = outageRecordsRepository

    def reportOutage(self):
        OutageReporter._logToStdout('OUTAGE!')
        
        if (self._outageDetected):
            self._updateCurrentOutageRecord()
        else:
            self._createNewOutageRecord()
        
        self._outageDetected = True

    def clearOutageStatus(self):
        if (self._outageDetected):
            OutageReporter._logToStdout('All clear.')

        self._outageDetected = False
    
    def _createNewOutageRecord(self):
        self._currentOutageStartTime = datetime.now()
        
        self._outageRecordsRepository.createNewOutage(self._currentOutageStartTime, outageEndDateTime=datetime.now())

    def _updateCurrentOutageRecord(self):
        self._outageRecordsRepository.updateOutageEndTimestamp(self._currentOutageStartTime, newOutageEndDateTime=datetime.now())

    @staticmethod
    def _logToStdout(message):
        print(OutageReporter._datetimeToStdoutStringFormat(datetime.now()) + ' ' + message, flush=True)
    
    @staticmethod
    def _datetimeToStdoutStringFormat(datetime):
        return datetime.strftime('%Y-%m-%d %H:%M:%S.%f')