class Container:
    def __init__(self, length, loadWeight=0):
        if not ((length == 20 and loadWeight <= 20) or (length == 40 and loadWeight <= 22)):
            raise ValueError(
                "Invalid input, either length 20 and load <= 20 or length 40 and load <= 22")
        self._length = length
        if length == 20:
            self._weight = 2
        else:
            self._weight = 4
        self._loadWeight = loadWeight
        self._serialNumber = ContainerManager_NewSerialNumber()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def loadWeight(self):
        return self._loadWeight

    @property
    def totalWeight(self):
        totalWeight = self.weight + self.loadWeight
        return totalWeight

    @loadWeight.setter
    def loadWeight(self, loadWeight):
        self._loadWeight = loadWeight

    @property
    def serialNumber(self):
        return self._serialNumber

    def __repr__(self):
        return f"{self.length} + {self.weight + self.loadWeight}"


ContainerManager_year = 2023
ContainerManager_month = 1
ContainerManager_day = 27
ContainerManager_number = 0


def ContainerManager_NewSerialNumber():
    global ContainerManager_year
    global ContainerManager_month
    global ContainerManager_day
    global ContainerManager_number
    ContainerManager_number += 1
    serialNumber = "{0:d}-{1:02d}-{2:d}-{3:04d}".format(
        ContainerManager_year, ContainerManager_month, ContainerManager_day, ContainerManager_number)
    return serialNumber
