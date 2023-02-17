from ships import ContainerShip
from container import Container

import random

# Container
# ---------------
containersInTrondheim = []


def addContainer(container=0):
    if container == 0:
        container = generateRandomContainer()
        containersInTrondheim.append(container)
    else:
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

# Docks
# --------------------


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


def task2():
    c1 = Container(20, 14)
    c2 = Container(40, 17)
    c3 = Container(20, 3)
    c4 = Container(40, 0)

    addContainer(c1)
    addContainer(c2)
    addContainer(c3)
    addContainer(c4)

    print("Task 2")

    print("Containers in Trondheim: ", containersInTrondheim)
    print()

    removeContainer(c1.serialNumber)
    removeContainer(c3.serialNumber)

    print("Containers in Trondheim (after remove): ", containersInTrondheim)
    print()

    container = getContainer(c2.serialNumber)
    print("Getting the container: ", container)
    print()


def task3():
    print("Task 3")
    randomContainer = generateRandomContainer()

    print("Random container: ", randomContainer.serialNumber,
          randomContainer.length, randomContainer.totalWeight)

    randomContainerSet = generateRandomContainerSet(10)

    print("Random container set: ", randomContainerSet)
    print()


def task4():
    print("Task 4")
    setOfContainers = generateRandomContainerSet(20)
    printToFile_Container(setOfContainers)

    loadedSet = loadFromFile_Container()
    print(loadedSet)
    print()


def task5():
    ship = ContainerShip(24, 22, 18)
    print("\n Task 5:\n")
    # Looks for container in ship
    test_container = Container(40, 10)
    ship.loadNewContainer(test_container)
    stack, indexOfContainer = ship.lookForContainer(
        test_container.serialNumber)
    print(
        f"Placement of container (stack, index in stack): {stack, indexOfContainer}")

    # Look for a place where a container (cell) can be loaded:
    test_cell = [Container(20, 5), Container(20, 10)]
    stack, indexOfContainer = ship.getOptimalLoadPlacementForContainer(
        test_cell)
    print(
        f"Available place for container cell (stack, index in stack): {stack, indexOfContainer}")

    # Load a container into ship:


def task6And7():

    print("\n Task 6 and 7:\n")
    # Loading a ship with 24 containers and returns the corresponding ordered list of containers
    ship = ContainerShip(24, 22, 18)
    ship.loadNewContainerSet(generateRandomContainerSet(24))
    print("Front left: ")
    print(f"{ship.frontLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.frontLeft)}")
    print("Front right: ")
    print(f"{ship.frontRight} Sectionweight: {ship.getTotalWeightOfSection(ship.frontRight)}")
    print("Middle left")
    print(f"{ship.middleLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.middleLeft)}")
    print("Middle right")
    print(f"{ship.middleRight} Sectionweight: {ship.getTotalWeightOfSection(ship.middleRight)}")
    print("Rear left")
    print(f"{ship.rearLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.rearLeft)}")
    print("Rear right")
    print(f"{ship.rearRight} Sectionweight: {ship.getTotalWeightOfSection(ship.rearRight)}")

    # Prints all containers on the ship to a file
    ship.printToFile_Ship("Containers_on_ship.csv")

    # Unloads the ship
    ship.removeAllContainersFromShip()
    print("Front left: ")
    print(ship.frontLeft)
    print(f"{ship.frontLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.frontLeft)}")
    print("Front right: ")
    print(f"{ship.frontRight} Sectionweight: {ship.getTotalWeightOfSection(ship.frontRight)}")
    print("Middle left")
    print(f"{ship.middleLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.middleLeft)}")
    print("Middle right")
    print(f"{ship.middleRight} Sectionweight: {ship.getTotalWeightOfSection(ship.middleRight)}")
    print("Rear left")
    print(f"{ship.rearLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.rearLeft)}")
    print("Rear right")
    print(f"{ship.rearRight} Sectionweight: {ship.getTotalWeightOfSection(ship.rearRight)}")

    # Loads the ship with the containers from the file
    ship.loadFromFile_Ship("Containers_on_ship.csv")
    print("Front left: ")
    print(f"{ship.frontLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.frontLeft)}")
    print("Front right: ")
    print(f"{ship.frontRight} Sectionweight: {ship.getTotalWeightOfSection(ship.frontRight)}")
    print("Middle left")
    print(f"{ship.middleLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.middleLeft)}")
    print("Middle right")
    print(f"{ship.middleRight} Sectionweight: {ship.getTotalWeightOfSection(ship.middleRight)}")
    print("Rear left")
    print(f"{ship.rearLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.rearLeft)}")
    print("Rear right")
    print(f"{ship.rearRight} Sectionweight: {ship.getTotalWeightOfSection(ship.rearRight)}")


def task9():
    print("\nTask 9:\n")
    ship = ContainerShip(24, 22, 18)
    ship.loadNewContainerSet(generateRandomContainerSet(10000))
    print("Front left: ")
    print(f"{ship.frontLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.frontLeft)}")
    print("Front right: ")
    print(f"{ship.frontRight} Sectionweight: {ship.getTotalWeightOfSection(ship.frontRight)}")
    print("Middle left")
    print(f"{ship.middleLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.middleLeft)}")
    print("Middle right")
    print(f"{ship.middleRight} Sectionweight: {ship.getTotalWeightOfSection(ship.middleRight)}")
    print("Rear left")
    print(f"{ship.rearLeft} Sectionweight: {ship.getTotalWeightOfSection(ship.rearLeft)}")
    print("Rear right")
    print(f"{ship.rearRight} Sectionweight: {ship.getTotalWeightOfSection(ship.rearRight)}")
    print(f"Total weight of ship: {ship.getTotalWeightOfShip()}")


def task11and12():
    print("\nTask 11 and 12:\n")
    ship = ContainerShip(24, 22, 18)
    ship.loadNewContainerSet(generateRandomContainerSet(10000))
    print(
        f"Total loading time of ship using four cranes: {fourCranesLoadingTime(ship)}")
    print(
        f"Total loading time of ship using one crane: {singleCraneLoadingTime(ship)}")


# task2()
# task3()
# task4()
# task5()
# task6And7()
# task9()
# task11and12()
