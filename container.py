import random
import csv


class Container:
    def __init__(self, serialNumber, length, loadWeight=0):
        if not ((length == 20 and loadWeight <= 20) or (length == 40 and loadWeight <= 22)):
            raise ValueError(
                "Invalid input, either length 20 and load <= 20 or length 40 and load <= 22")
        self._length = length
        if length == 20:
            self._weight = 2
        else:
            self._weight = 4
        self._loadWeight = loadWeight
        self._serialNumber = serialNumber
        allContainers.add(self)

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

    @loadWeight.setter
    def loadWeight(self, loadWeight):
        self._loadWeight = loadWeight

    @property
    def serialNumber(self):
        return self._serialNumber

    def __repr__(self):
        return f"{self.serialNumber}"


def addContainer(serialNumber):
    for container in allContainers:
        if container.serialNumber == serialNumber:
            containersInTrondheim.append(container)
            return
    raise ValueError("Container does not exist")


def removeContainer(serialNumber):
    for container in containersInTrondheim:
        if container.serialNumber == serialNumber:
            containersInTrondheim.remove(container)
            return
    raise ValueError("Container is not in Trondheim harbor")


def getContainer(serialNumber):
    for container in containersInTrondheim:
        if container.serialNumber == serialNumber:
            return container
    raise ValueError("Container is not in Trondheim harbor")


def generateRandomContainer():
    serialNumber = ContainerManager_NewSerialNumber()
    if random.randint(0, 1) == 0:
        load = random.randrange(0, 21)
        return Container(serialNumber, 20, load)
    else:
        load = random.randrange(0, 23)
        return Container(serialNumber, 40, load)


def generateRandomContainerSet(n):
    if n <= 0:
        raise ValueError("Input must be 1 or above")
    randomContainerSet = []
    for i in range(n):
        randomContainerSet.append(generateRandomContainer())
    return randomContainerSet


# 5. Container Manager
# --------------------

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


def writeToFile(containerSet):
    f = open("containers.csv", "w", newline="")
    writer = csv.writer(f)
    tup1 = ("Unique code", "length", "weight", "loadWeight")
    writer.writerow(tup1)
    for container in containerSet:
        tuple = (container.serialNumber, container.length,
                 container.weight, container.loadWeight)
        writer.writerow(tuple)

    f.close()


containersInTrondheim = []
allContainers = set()

# Main
# --------------------


container1 = generateRandomContainer()
container2 = generateRandomContainer()
container3 = generateRandomContainer()
container4 = generateRandomContainer()

print(f"{container1.length} + {container1.weight} + {container1.loadWeight} + {container1.serialNumber}")
print(f"{container2.length} + {container2.weight} + {container2.loadWeight} + {container2.serialNumber}")

print(allContainers)
print(containersInTrondheim)
addContainer(container1.serialNumber)
addContainer(container2.serialNumber)
print(containersInTrondheim)
# removeContainer(1)
print(containersInTrondheim)
print(allContainers)
print(generateRandomContainerSet(10))
writeToFile(generateRandomContainerSet(5))
