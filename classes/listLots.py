class ListLots:
    def __init__(self):
        self.__list = []
        self.__batchNumber = 0

    def addBatch(self, batch):
        self.__list.append(batch)
        self.__batchNumber = self.__batchNumber + 1

    def getActualListLots(self):
        if self.__batchNumber > 0:
            return self.__list[0]

    def deleteActualProcess(self):
        if self.__batchNumber > 0:
            numberPendingProcess = self.__list[0].numberProcess()
            if numberPendingProcess == 0:
                self.__list.pop(0)
                self.__batchNumber -= 1

    def numberBatch(self):
        return self.__batchNumber
