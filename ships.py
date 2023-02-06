from container import Container
# import main

class ContainerShip:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height
        
        sectionWidth = width//2
        sectionLength = length//3
        self._frontLeft = [[0] for _ in range(sectionWidth * sectionLength)]
        self._frontRight = [[0] for _ in range(sectionWidth * sectionLength)]
        self._middleRight = [[0] for _ in range(sectionWidth * sectionLength)]
        self._middleLeft = [[0] for _ in range(sectionWidth * sectionLength)]
        self._rearRight = [[0] for _ in range(sectionWidth * sectionLength)]
        self._rearLeft = [[0] for _ in range(sectionWidth * sectionLength)]
        self._sections = [self._frontLeft, self._frontRight, self._middleLeft, self._middleRight, self._rearLeft, self._rearRight]
        
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
    
    def getTotalWeightOfSection(self, section):
        totalWeight = 0
        for stack in section:
            totalWeight += self.getTotalWeightOfStack(stack)
        return totalWeight

    def getLightestSection(self):
        lightestSection = self.frontLeft
        for section in self.sections:
            if self.getTotalWeightOfSection(section) < self.getTotalWeightOfSection(lightestSection):
                lightestSection = section
        return lightestSection
    
    def getTotalWeightOfStack(self, stack):
        totalWeight = 0
        for container in stack:
            if container != 0:
                totalWeight += container.totalWeight
        return totalWeight
        
    def getLightestAvailableStackInSection(self, section):
        lightestAvailableStack = section[0]
        for stack in section:
            if self.getTotalWeightOfStack(stack) < self.getTotalWeightOfStack(lightestAvailableStack) and (stack[-1] == 0):
                lightestAvailableStack = stack
        return lightestAvailableStack
    
    def getOptimalLoadPlacementForContainer(self, container):
        lightestSection = self.getLightestSection()
        lightestStack = self.getLightestAvailableStackInSection(lightestSection)
        for i in range(len(lightestStack)):
            if lightestStack[i] == 0 or lightestStack[i].totalWeight < container.totalWeight:
                return lightestStack, i
                # lightestStack.insert(i, container)
    
    def loadNewContainer(self, container):
        stack, index = self.getOptimalLoadPlacementForContainer(container)
        if index == (self.height -1):
            stack[-1] = container
        else:
            stack.insert(index, container)
        
    def loadNewContainerSet(self, containers):
        for container in containers:
            self.loadNewContainer(container)

    def look_for_container(self, serialNumber):
        for section in self.sections:
            for stack in section:
                for container in stack:
                    if container.serialNumber is not None and container.serialNumber == serialNumber:
                        return stack, stack.index(container), container
        raise ValueError("Container could not be found on the ship")
        

    def unload_container(self, serialNumber):
        position = self.look_for_container(serialNumber)
        if position is not None:
            stack, index = position
            container = stack.pop(index)
            # main.containersInTrondheim.append(container)

            
    # def print_to_file(self, file_name):
    #     with open(file_name, 'w') as f:
    #         for l in range(self.length):
    #             for w in range(self.width):
    #                 for h in range(self.height):
    #                     if self.bays[l][w][h] is not None:
    #                         f.write(str(l) + ' ' + str(w) + ' ' + str(h) + ' ' + self.bays[l][w][h].get_code() + '\n')

    # def load_from_file(self, file_name):
    #     with open(file_name, 'r') as f:
    #         for line in f:
    #             l, w, h, code = line.strip().split()
    #             container = ContainerSet.look_for_container(code)
    #             self.load_container(container, (int(l), int(w), int(h)))
    
    # def load_from_set(self, container_set):
    #     containers = container_set.get_containers()
    #     loaded_containers = []
    #     for container in containers:
    #         position = self.look_for_place(container)
    #         if position is not None:
    #             self.load_container(container, position)
    #             loaded_containers.append(container)
    #     return loaded_containers


# Main
# -----------------


    