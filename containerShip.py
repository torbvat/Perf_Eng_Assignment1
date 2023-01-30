# TPK4186 - 2023 - Assignment 1

# 1. Imported modules
# -------------------

import sys
import random

# 2. Containers
# -------------


def Container_New(serialNumber, length, weight, cargo):
    # Require: 0 <= cargo <= 22
    return [serialNumber, length, weight, cargo]


def Container_NewSmall(serialNumber, cargo):
    return Container_New(serialNumber, 20, 2, cargo)


def Container_NewBig(serialNumber, cargo):
    return Container_New(serialNumber, 40, 4, cargo)


def Container_GetSerialNumber(container):
    return container[0]


def Container_SetSerialNumber(container, serialNumber):
    container[0] = serialNumber


def Container_GetLength(container):
    return container[1]


def Container_SetLength(container, length):
    container[1] = length


def Container_GetWeight(container):
    return container[2]


def Container_SetWeight(container, weight):
    container[2] = weight


def Container_GetCargo(container):
    return container[3]


def Container_SetCargo(container, cargo):
    container[3] = cargo


def Container_GetTotalWeight(container):
    return Container_GetWeight(container) + Container_GetCargo(container)

# 3. Ships
# --------


def Ship_New(length, width, height):
    return [length, width, height, []]


def Ship_GetLength(ship):
    return ship[0]


def Ship_SetLength(ship, length):
    ship[0] = length


def Ship_GetWidth(ship):
    return ship[1]


def Ship_SetWidth(ship, width):
    ship[1] = width


def Ship_GetHeight(ship):
    return ship[2]


def Ship_SetHeight(ship, height):
    ship[2] = height


def Ship_GetContainers(ship):
    return ship[3]


def Ship_GetNumberOfContainers(ship):
    return len(Ship_GetContainers(ship))


def Ship_GetNthContainer(ship, index):
    containers = Ship_GetContainers(ship)
    return containers[index]


def Ship_InsertContainer(ship, container, index):
    containers = Ship_GetContainers(ship)
    containers.insert(index, container)


def Ship_AppendContainer(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)


def Ship_LoadContainer(ship, newContainer):
    newContainerWeight = Container_GetTotalWeight(newContainer)
    loaded = False
    i = 0
    while i < Ship_GetNumberOfContainers(ship):
        container = Ship_GetNthContainer(ship, i)
        containerWeight = Container_GetTotalWeight(container)
        if containerWeight <= newContainerWeight:
            Ship_InsertContainer(ship, newContainer, i)
            loaded = True
            break
        i = i + 1
    if not loaded:
        Ship_AppendContainer(ship, newContainer)


def Ship_IsEmpty(ship):
    return Ship_GetNumberOfContainers(ship) == 0


def Ship_PushContainer(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)


def Ship_PushContainers(ship, containers):
    while len(containers) != 0:
        container = containers.pop()
        Ship_PushContainer(ship, container)


def Ship_PopContainer(ship):
    if Ship_GetNumberOfContainers(ship) == 0:
        return
    containers = Ship_GetContainers(ship)
    containers.pop()


def Ship_PopLighterContainers(ship, thresholdWeight):
    poppedContainers = []
    while not Ship_IsEmpty(ship):
        container = Ship_GetTopContainer(ship)
        totalWeight = Container_GetTotalWeight(container)
        if totalWeight >= thresholdWeight:
            break
        Ship_PopContainer(ship)
        poppedContainers.append(container)
    return poppedContainers


def Ship_GetTopContainer(ship):
    if Ship_GetNumberOfContainers(ship) == 0:
        return None
    containers = Ship_GetContainers(ship)
    return containers[-1]


def Ship_PileContainer(ship, container):
    totalWeightContainer = Container_GetTotalWeight(container)
    poppedContainers = Ship_PopLighterContainers(ship, totalWeightContainer)
    Ship_PushContainer(ship, container)
    Ship_PushContainers(ship, poppedContainers)


# 4: Printer
# ----------

def Printer_PrintContainer(container):
    serialNumber = Container_GetSerialNumber(container)
    length = Container_GetLength(container)
    weight = Container_GetWeight(container)
    cargo = Container_GetCargo(container)
    totalWeight = Container_GetTotalWeight(container)
    print(str(serialNumber) + " " + str(length) + " " +
          str(weight) + " " + str(cargo) + " " + str(totalWeight))


def Printer_PrintShip(ship):
    length = Ship_GetLength(ship)
    width = Ship_GetWidth(ship)
    height = Ship_GetHeight(ship)
    containers = Ship_GetContainers(ship)
    print("Ship")
    print(str(length) + " " + str(width) + " " + str(height))
    print("Containers")
    for container in containers:
        Printer_PrintContainer(container)

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


def ContainerManager_NewRandomContainer():
    serialNumber = ContainerManager_NewSerialNumber()
    isSmall = random.randint(0, 1)
    if isSmall == 0:
        cargo = random.randint(0, 20)
        container = Container_NewSmall(serialNumber, cargo)
    else:
        cargo = random.randint(0, 22)
        container = Container_NewBig(serialNumber, cargo)
    return container


# X. Main
# -------

ship = Ship_New(23, 22, 18)
for i in range(0, 10000):
    container = ContainerManager_NewRandomContainer()
    Ship_PileContainer(ship, container)

Printer_PrintShip(ship)
