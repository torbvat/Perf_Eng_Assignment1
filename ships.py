from container import Container
import math
# import main


class ContainerShip:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

        cellWidth = width//2
        cellLength = length//6
        self._frontLeft = [[[0, 0]]*height
                           for _ in range(cellWidth * cellLength)]
        self._frontRight = [[[0, 0]]*height
                            for _ in range(cellWidth * cellLength)]
        self._middleRight = [[[0, 0]]*height
                             for _ in range(cellWidth * cellLength)]
        self._middleLeft = [[[0, 0]]*height
                            for _ in range(cellWidth * cellLength)]
        self._rearRight = [[[0, 0]]*height
                           for _ in range(cellWidth * cellLength)]
        self._rearLeft = [[[0, 0]]*height
                          for _ in range(cellWidth * cellLength)]
        self._sections = [self._frontLeft, self._frontRight, self._middleLeft,
                          self._middleRight, self._rearLeft, self._rearRight]
        self._singleContainers = []

        self._nrOfContainersOnShip = 0

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def frontLeft(self):
        return self._frontLeft

    @property
    def frontRight(self):
        return self._frontRight

    @property
    def middleLeft(self):
        return self._middleLeft

    @property
    def middleRight(self):
        return self._middleRight

    @property
    def rearLeft(self):
        return self._rearLeft

    @property
    def rearRight(self):
        return self._rearRight

    @property
    def sections(self):
        return self._sections

    @property
    def singleContainers(self):
        return self._singleContainers

    @singleContainers.setter
    def singleContainers(self, singleContainers):
        self._singleContainers = singleContainers

    @property
    def nrOfContainersOnShip(self):
        return self._nrOfContainersOnShip

    def addContainerToShip(self, containerCell):
        if containerCell[0].length == 20:
            self._nrOfContainersOnShip += 2
        else:
            self._nrOfContainersOnShip += 1

    def isAboveMinAmountOfContainers(self):
        return self.nrOfContainersOnShip >= self.height*self.width*self.length/2.5

    def hasSingleOnHold(self):
        if len(self.singleContainers) == 0:
            return False
        else:
            return True

    def emptySingleContainers(self):
        self.singleContainers = []

    def isEmptyCell(self, containerCell):
        if containerCell[0] == 0 and containerCell[1] == 0:
            return True
        else:
            return False

    def getTotalWeightOfCell(self, containerCell):
        totalWeight = 0
        if not self.isEmptyCell(containerCell):
            totalWeight += containerCell[0].totalWeight
            if containerCell[0].length == 20:
                totalWeight += containerCell[1].totalWeight

        return totalWeight

    def getTotalWeightOfStack(self, stack):
        totalWeight = 0
        for containerCell in stack:
            totalWeight += self.getTotalWeightOfCell(containerCell)
        return totalWeight

    def getTotalWeightOfSection(self, section):
        totalWeight = 0
        for stack in section:
            totalWeight += self.getTotalWeightOfStack(stack)
        return totalWeight

    def getStarboardWeight(self):
        return self.getTotalWeightOfSection(self.frontRight) + self.getTotalWeightOfSection(self.middleRight) + self.getTotalWeightOfSection(self.rearRight)

    def getPortsideWeight(self):
        return self.getTotalWeightOfSection(self.frontLeft) + self.getTotalWeightOfSection(self.middleLeft) + self.getTotalWeightOfSection(self.rearLeft)

    def isStackFull(self, stack):
        return not stack[-1] == [0, 0]

    def isSectionFull(self, section):
        for stack in section:
            if not self.isStackFull(stack):
                return False
        return True

    def isShipFull(self):
        for section in self.sections:
            if not self.isSectionFull(section):
                return False
        return True

    def checkSideBalance(self):
        return not (math.abs(self.getStarboardWeight()-self.getPortsideWeight()) >= self.getStarboardWeight/20)

    def checkSectionBalance(self):
        for sectionI in self.sections:
            for sectionJ in self.sections:
                if math.abs(self.getTotalWeightOfSection(sectionI)-self.getTotalWeightOfSection(sectionJ)) >= self.getTotalWeightOfSection/10:
                    return False
        return True

    def isShipBalanced(self):
        return self.checkSideBalance() and self.checkSectionBalance()

    def getStacksInSectionWithAvailableSpace(self, section):
        #return list(stack for stack in section if not self.isStackFull(stack))

        stacksWithAvailableSpace = []
        for stack in section:
            if not self.isStackFull(stack):
                stacksWithAvailableSpace.append(stack)
        return stacksWithAvailableSpace

    def getSectionsWithAvailableSpace(self):
        sectionsWithAvailableSpace = []
        for section in self.sections:
            if not self.isSectionFull(section):
                sectionsWithAvailableSpace.append(section)
        return sectionsWithAvailableSpace

    # Returns the lightest stack in a section with available space
    def getLightestAvailableStackInSection(self, section):
        stacksInSectionWithAvailableSpace = self.getStacksInSectionWithAvailableSpace(
            section)
        if not len(stacksInSectionWithAvailableSpace):
            return []

        lightestAvailableStack = stacksInSectionWithAvailableSpace[0]

        for stack in stacksInSectionWithAvailableSpace:
            if (self.getTotalWeightOfStack(stack) < self.getTotalWeightOfStack(lightestAvailableStack)):
                lightestAvailableStack = stack
        if self.isStackFull(lightestAvailableStack):
            print(lightestAvailableStack[-1])
            raise ValueError("No available space in section")
        return lightestAvailableStack
    
        
    def getLightestAvailableSection(self):
        sectionsWithAvailableSpace = [section for section in self.sections if not self.isSectionFull(section)]
        if not sectionsWithAvailableSpace:
            raise ValueError("No available space in ship")
        lightestAvailableSection = sectionsWithAvailableSpace[0]
        for section in sectionsWithAvailableSpace:
            if self.getTotalWeightOfSection(section) < self.getTotalWeightOfSection(lightestAvailableSection):
                lightestAvailableSection = section
        return lightestAvailableSection

    def getOptimalLoadPlacementForContainer(self, containerCell):
        if self.isShipFull():
            raise ValueError("Ship is full")
        
        lightestSection = self.getLightestAvailableSection()
        if not lightestSection:
            return [], None
        
        lightestStack = self.getLightestAvailableStackInSection(lightestSection)
        if not lightestStack:
            return [], None
        
        for i in range(len(lightestStack)):
            if self.isEmptyCell(lightestStack[i]) or self.getTotalWeightOfCell(lightestStack[i]) < self.getTotalWeightOfCell(containerCell):
                return lightestStack, i

    def loadNewContainer(self, container):
        if self.isShipFull():
            print("Ship is full!")
            return
        containerCell = []
        if container.length == 20:
            if self.hasSingleOnHold():
                containerCell = self.singleContainers
                self.emptySingleContainers()
                containerCell.append(container)
            else:
                self.singleContainers.append(container)
                return
        else:
            containerCell = [container, container]

        stack, index = self.getOptimalLoadPlacementForContainer(containerCell)
        if len(stack) == 0 or index is None:
            print(
                f"Ship is full, with {self.nrOfContainersOnShip} containers on it")
            return
        if index == (self.height - 1):
            stack[-1] = containerCell
        else:
            stack.insert(index, containerCell)
            stack.pop(-1)

        self.addContainerToShip(containerCell)

    def loadNewContainerSet(self, containers):
        for container in containers:
            if self.isShipFull():
                print("Ship is full")
                return
            else:
                self.loadNewContainer(container)

    def lookForContainer(self, serialNumber):
        for section in self.sections:
            for stack in section:
                for containerCell in stack:
                    for container in containerCell:
                        if container != 0 and container.serialNumber == serialNumber:
                            return stack, stack.index(containerCell)
        raise ValueError("Container could not be found on the ship")

    def unloadContainer(self, serialNumber):
        position = self.lookForContainer(serialNumber)
        if position is not None:
            stack, index = position
            containerCell = stack.pop(index)
            stack.append([0, 0])
            if containerCell[0].length == 20:
                if containerCell[0].serialNumber == serialNumber:
                    self.loadNewContainer(containerCell[1])
                else:
                    self.loadNewContainer(containerCell[0])

    # Prints the load of the ship to a file. Does not impact the load of the ship.
    def print_to_file(self):
        with open("containers_on_ship.csv", "w") as f:
            for section in self.sections:
                for stack in section:
                    for containerCell in stack:
                        if containerCell[0] is not None and containerCell[0] != 0:
                            f.write(
                                f"{containerCell[0]._length}\t{containerCell[0].loadWeight}\t{containerCell[0]._serialNumber}\n")
                        if containerCell[1] is not None and containerCell[1] != 0 and containerCell[1]._length == 20:
                            f.write(
                                f"{containerCell[1]._length}\t{containerCell[1].loadWeight}\t{containerCell[1]._serialNumber}\n")

    # Loads the containers from the file onto the ship.
    def load_from_file(self):
        with open("containers_on_ship.csv", "r") as f:
            for line in f:
                length, loadWeight, serialNumber = line.strip().split("\t")
                container = Container(
                    int(length), int(loadWeight), serialNumber)
                self.loadNewContainer(container)
