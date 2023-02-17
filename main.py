from ships import ContainerShip
from container import Container

import random

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

# Container Manager
# --------------------


def printToFile_Container(containerSet):
    with open("containers.csv", "w") as f:
        for container in containerSet:
            f.write(
                f"{container.length}\t{container.weight}\t{container.loadWeight}\t{container.serialNumber}\n")


def loadFromFile_Container():
    containerSet = []
    with open("containers.csv", "r") as f:
        for line in f:
            line = line.split("\t")
            container = Container(int(line[0]), int(line[2]), line[3])
            containerSet.append(container)
    return containerSet


containersInTrondheim = []

# --------------------
# Docks


def singleCraneLoadingTime(ship):
    loadingTime = ship.nrOfContainersOnShip * 4
    return loadingTime


def fourCranesLoadingTime(ship):
    loadingTime = 0
    ordered_containerCells = []
    amountOfContainersInSections = {
        "containersInSection1": 0, "containersInSection2": 0, "containersInSection3": 0, "containersInSection4": 0}
    for section in ship._sections:
        for stack in section:
            for containerCell in stack:
                ordered_containerCells.append(containerCell)
    for i in range(4):
        for containerCell in ordered_containerCells[len(ordered_containerCells)//4*i:len(ordered_containerCells)//4*(i+1)]:
            if not containerCell == [0, 0]:
                if containerCell[1].length == 20:
                    amountOfContainersInSections["containersInSection" +
                                                 str(i+1)] += 2
                elif containerCell[1].length == 40:
                    amountOfContainersInSections["containersInSection" +
                                                 str(i+1)] += 1
                else:
                    continue
    amountOfContainersInSectionWithMostContainers = max(
        amountOfContainersInSections.values())
    # Assuming that the restrictions for the cranes are satisfied without time delay:
    loadingTime = amountOfContainersInSectionWithMostContainers * 4
    return loadingTime

# Main
# --------------------


ship1 = ContainerShip(24, 22, 18)

ship1.loadNewContainerSet(generateRandomContainerSet(8000))

print(ship1.hasSingleOnHold())
print("Front left: ")
print(f"{ship1.frontLeft} Sectionweight: {ship1.getTotalWeightOfSection(ship1.frontLeft)}")
print("Front right: ")
print(f"{ship1.frontRight} Sectionweight: {ship1.getTotalWeightOfSection(ship1.frontRight)}")
print("Middle left")
print(f"{ship1.middleLeft} Sectionweight: {ship1.getTotalWeightOfSection(ship1.middleLeft)}")
print("Middle right")
print(f"{ship1.middleRight} Sectionweight: {ship1.getTotalWeightOfSection(ship1.middleRight)}")
print("Rear left")
print(f"{ship1.rearLeft} Sectionweight: {ship1.getTotalWeightOfSection(ship1.rearLeft)}")
print("Rear right")
print(f"{ship1.rearRight} Sectionweight: {ship1.getTotalWeightOfSection(ship1.rearRight)}")

print(
    f"Amount of containers on ship: {ship1.nrOfContainersOnShip} containers.")
print("Minutes used to load or unload the ship with a single crane: ",
      singleCraneLoadingTime(ship1))
print("Minutes used to load or unload the ship with four cranes: ",
      fourCranesLoadingTime(ship1))

print()
# containersInTrondheim.append(ship1.removeAllContainersFromShip())
# print(containersInTrondheim)

ship1.printToFile_Ship()
