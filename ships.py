from container import Container, ContainerSet


#Finn ei løsning for 40-fots containere, mhp at de tar opp 2 celler/bays
class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.bays = [[[None for _ in range(height)] for _ in range(width)] for _ in range(length)]

    def get_ship_length(self):
        return self.length   

    def get_ship_width(self):
        return self.width  

    def get_ship_height(self):
        return self.height     
        
    #Returnerer posisjonen til en container i skipet, gitt ved (lengde, bredde, høyde)    
    def look_for_container(self, code):
        for l in range(self.length):
            for w in range(self.width):
                for h in range(self.height):
                    if self.bays[l][w][h] is not None and self.bays[l][w][h].get_code() == code:
                        return (l,w,h)
        return None

    #TODO: Fiks importering av Container klasse, av en el anna grunn funka ikkje getters    
    #Returnerer posisjonen til en ledig plass i skipet, gitt ved (lengde, bredde, høyde)       
    def look_for_place(self, container):
        for l in range(self.length):
            for w in range(self.width):
                for h in range(self.height):
                    if self.bays[l][w][h] is None or self.bays[l][w][h].get_length() == container.get_length():
                        return (l,w,h)
        return None
    
    #TODO: "Note that it is not possible to load a 40 feet container onto a single 20 feet container
    #(there should no holes)."
    def load_container(self, container, position):
        l,w,h = position
        if(self.bays[l][w][h-1] is None):
            raise ValueError("There should be no empty bays under the container you are loading onto the ship")
        self.bays[l][w][h] = container
    
    def remove_container(self, code):
        position = self.look_for_container(code)
        if position is not None:
            l,w,h = position
            self.bays[l][w][h] = None
            
    def print_to_file(self, file_name):
        with open(file_name, 'w') as f:
            for l in range(self.length):
                for w in range(self.width):
                    for h in range(self.height):
                        if self.bays[l][w][h] is not None:
                            f.write(str(l) + ' ' + str(w) + ' ' + str(h) + ' ' + self.bays[l][w][h].get_code() + '\n')

    def load_from_file(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                l, w, h, code = line.strip().split()
                container = ContainerSet.look_for_container(code)
                self.load_container(container, (int(l), int(w), int(h)))
    
    def load_from_set(self, container_set):
        containers = container_set.get_containers()
        loaded_containers = []
        for container in containers:
            position = self.look_for_place(container)
            if position is not None:
                self.load_container(container, position)
                loaded_containers.append(container)
        return loaded_containers





    