import re


def check_serialNumber_format(serialNumber):
    match = re.match(r"\d{4}-\d{2}-\d{2}-\d{4}", str(serialNumber))
    return True if match else False


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


class Container:

    def __init__(self, length, loadWeight=0, serialNumber=None):
        if not ((length == 20 and loadWeight <= 20) or (length == 40 and loadWeight <= 22)):
            raise ValueError(
                "Invalid input, either length 20 and load <= 20 or length 40 and load <= 22")
        self._length = length
        if length == 20:
            self._weight = 2
        else:
            self._weight = 4
        self._loadWeight = loadWeight

        if(serialNumber == None):
            self._serialNumber = ContainerManager_NewSerialNumber()
        elif(str(check_serialNumber_format(serialNumber)) == False):
            raise ValueError("Invalid serial number format")
        else:
            self._serialNumber = serialNumber

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
        _totalWeight = self.weight + self.loadWeight
        return _totalWeight

    @loadWeight.setter
    def loadWeight(self, loadWeight):
        self._loadWeight = loadWeight

    @property
    def serialNumber(self):
        return self._serialNumber

    def __repr__(self):
        return f"{self.totalWeight}"
