from ships import ContainerShip
from container import Container

import random
import csv

# Container
# ---------------


def addContainer():
    container = generateRandomContainer()
    containersInTrondheim.append(container)


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
    if random.randint(0, 1) == 0:
        load = random.randrange(0, 21)
        return Container(20, load)
    else:
        load = random.randrange(0, 23)
        return Container(40, load)


def generateRandomContainerSet(n):
    if n <= 0:
        raise ValueError("Input must be 1 or above")
    randomContainerSet = []
    for i in range(n):
        randomContainerSet.append(generateRandomContainer())
    return randomContainerSet


# 5. Container Manager
# --------------------


def write_to_file(containerSet):
    with open("containers.csv", "w") as f:
        for container in containerSet:
            f.write(
                f"{container.length}\t{container.weight}\t{container.loadWeight}\t{container.serialNumber}\n")


def read_from_file():
    containerSet = []
    with open("containers.csv", "r") as f:
        for line in f:
            line = line.split("\t")
            container = Container(int(line[0]), int(line[2]), line[3])
            containerSet.append(container)
    return containerSet


containersInTrondheim = []
# Ship
# --------------------


# Main
# --------------------
"""
containerSet = generateRandomContainerSet(10)
print(containerSet)
write_to_file(containerSet)
print(read_from_file())
"""
# container1 = generateRandomContainer()
# container2 = generateRandomContainer()
# container3 = generateRandomContainer()
# container4 = generateRandomContainer()

# print(f"{container1.length} + {container1.weight} + {container1.loadWeight} + {container1.serialNumber}")
# print(f"{container2.length} + {container2.weight} + {container2.loadWeight} + {container2.serialNumber}")

# print(containersInTrondheim)
# addContainer()
# addContainer()
# print(containersInTrondheim)
# # removeContainer(1)
# print(containersInTrondheim)
# print(generateRandomContainerSet(10))
# writeToFile(generateRandomContainerSet(5))

# c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24 = generateRandomContainerSet(24)

print()

ship1 = ContainerShip(6, 4, 2)
c1 = Container(20, 14)
c2 = Container(40, 15)
c3 = Container(20, 12)
c4 = Container(20, 10)
c5 = Container(40, 2)
c6 = Container(40, 20)

cSet = [c1, c2, c3, c4, c5, c6]

ship1.loadNewContainerSet(cSet)


print(c1, c2, c3, c4, c5)

# ship1.loadNewContainerSet(generateRandomContainerSet(10000))
"""
ship1.print_to_file()
if(ship1.frontLeft[0][0][1]!=0):
    print(ship1.frontLeft[0][0][1].serialNumber)
ship2 = ContainerShip(6, 4, 4)
ship2.load_from_file()
if(ship2.frontLeft[0][0][1]!=0):
    print(ship2.frontLeft[0][0][1].serialNumber)
"""
"""
print(ship1.hasSingleOnHold())
print("Front left: ")
print(f"{ship1.frontLeft} weight: {ship1.getTotalWeightOfSection(ship1.frontLeft)}")
print("Front right: ")
print(f"{ship1.frontRight} weight: {ship1.getTotalWeightOfSection(ship1.frontRight)}")
print("Middle left")
print(f"{ship1.middleLeft} weight: {ship1.getTotalWeightOfSection(ship1.middleLeft)}")
print("Middle right")
print(f"{ship1.middleRight} weight: {ship1.getTotalWeightOfSection(ship1.middleRight)}")
print("Rear left")
print(f"{ship1.rearLeft} weight: {ship1.getTotalWeightOfSection(ship1.rearLeft)}")
print("Rear right")
print(f"{ship1.rearRight} weight: {ship1.getTotalWeightOfSection(ship1.rearRight)}")

print(ship1.lookForContainer("2023-01-27-0001"))
ship1.unloadContainer(c3.serialNumber)

print(ship1.hasSingleOnHold())
print("Front left: ")
print(f"{ship1.frontLeft} weight: {ship1.getTotalWeightOfSection(ship1.frontLeft)}")
print("Front right: ")
print(f"{ship1.frontRight} weight: {ship1.getTotalWeightOfSection(ship1.frontRight)}")
print("Middle left")
print(f"{ship1.middleLeft} weight: {ship1.getTotalWeightOfSection(ship1.middleLeft)}")
print("Middle right")
print(f"{ship1.middleRight} weight: {ship1.getTotalWeightOfSection(ship1.middleRight)}")
print("Rear left")
print(f"{ship1.rearLeft} weight: {ship1.getTotalWeightOfSection(ship1.rearLeft)}")
print("Rear right")
print(f"{ship1.rearRight} weight: {ship1.getTotalWeightOfSection(ship1.rearRight)}")
print(ship1.singleContainers)


"""
# c1, c2, c3 = generateRandomContainerSet(3)
# ship1 = ContainerShip(6, 4, 4)

# liste = [[c1, c1], [c2, c3]]
# print(f"{c1.length} + {c1.totalWeight}")
# print(f"{c2.length} + {c2.totalWeight}")
# print(f"{c3.length} + {c3.totalWeight}")
# print(ship1.getTotalWeightOfCell(liste[0]))

#--------------------
#Docks

def single_crane_loading_time(ship):
    loadingTime = ship.nrOfContainersOnShip * 4
    return loadingTime

def four_cranes_loading_time(ship):    
    #Four cranes will use at average one minute per container, but we'll add 5% to account for the restrictions of the cranes.
    #This is an estimate, based on the assumption that the container are equally distributed in the sections of the ship.
    loadingTime = ship.nrOfContainersOnShip*1.05 
    return loadingTime

print(ship1._nrOfContainersOnShip)
print("Minutes used to load or unload the ship with a single crane: ",single_crane_loading_time(ship1))
print("Minutes used to load or unload the ship with four cranes: ",four_cranes_loading_time(ship1))
