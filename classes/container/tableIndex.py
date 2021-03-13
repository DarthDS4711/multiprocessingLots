class TableIndex:
    def __init__(self):
        self.__listIndex = []

    def addItem(self, item):
        self.__listIndex.append(item)

    def searchItem(self, item):
        self.__listIndex.sort()
        left = 0
        rigth = len(self.__listIndex) - 1
        notFinded = True
        while (left <= rigth) and notFinded:
            medium = (left + rigth) // 2
            itemList = self.__listIndex[medium]
            if (item == itemList):
                notFinded = False
            elif (item < itemList):
                rigth = medium - 1
            else:
                left = medium + 1
        return notFinded

