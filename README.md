# Perf_Eng_Assignment1

Assumptions:
    -For simplicity we assume the size of the ship has the following dimensions:
        -L: 24
        -W: 22
        -H: 18
It is of course possible to create a ship with smaller dimensions as long as the length is divisible by 6, and the width is an even number. However, when creating a smaller ship the weight balancing will be thrown off, because of how there needs to be enough containers for the load to be properly balanced. Therefore the ship probably will not be completely filled if it has much smaller dimensions, as the balancing check will kick in.
    -The ship will not leave without a certain amount of containers loaded on it, and therefore we do not check for weight balance before that amount is reached. This is also partially because there has to be a minimum amount of containers on the ship for the imbalance in loading to affect the ships balance.
-----------------------------------------------------------------------------------------------------------------------------

About our solution:
    Container:
        -Each container is represented like this: “Length + TotalWeight”, but they all have a unique serial number which can easily be retrieved.
    
    Structure of the ship:
        -We decided to divide our ship into six sections: frontLeft, frontRight, middleLeft, middleRight, rearLeft and rearRight. Each section is then divided into stacks, which are columns of containerCells. The stacks used are lists with the container at index 0 being the bottom and therefore the heaviest container in the stack. Each stack consists of containerCells which are 40 feet long, 20 feet wide and 20 feet tall. The cells are on the form [0, 0], and if we are loading a 40 feet long container, both cells are represented by that container like this: [container1, container1]. When loading 20 feet containers we exclusively load these in pairs to avoid any “holes”, and we therefore wait until there comes another 20 feet container which we can load it together with. Then the containerCell will look like this [container2, container3]. If the ship is filled up without getting a second 20 feet container to create the pair, we do not load the single container at all.
    
    Loading new containers
        -For every container that is to be loaded on a ship, we find the lightest available stack in the lightest available section on the ship, and create containerCells which are inserted between containers that weigh more and less than the new containerCell. Available stacks and sections are those with room for one or more additional containerCells. This greedy algorithm ensures a certain amount of stability between sections and sides, as well as the weight of the containerCells increasing for each row we move up. Because of the amount of containers which are to be loaded on the ship, a significant imbalance is incredibly unlikely.
    
    Unloading containers
        -When unloading a container we first look for the placement of the container with that specific serialNumber. When it is located we pop the whole stack from the cell, making sure there are still no holes. If the container is 20 feet long the other container in the pair is attempted to be reloaded as all other containers.

    Ensuring balance
        -Despite it being incredibly unlikely that the loading ends up being significantly unbalanced, we have implemented a method to make sure that it does not happen. When the minimum amount of containers is reached we start checking for imbalance for every container, and go on to search for a lighter container which does not cause imbalance.
            -Values used in balancing:
                -For checking the balance of the sections and sides of the ship, we have decided upon a threshold of 5% difference between starboard and portside, and 10% difference between the three sections.
                -We have set a minimum amount of containers to L*W*(H/2)/2.5 for no particular reason, other than there being enough containers to check for imbalance while still not being too many leading to checking the balance too late.

    Docks
        -For the docks, we do not know the exact amount of containers which are going to be loaded onto the ship, as the amount of 20- and 40-foot containers will vary, and the balancing might affect the number of containers. Therefore, our code is meant as a simulation of the load, so that we know the amount of containers. For one crane we get the amount of containers times 4 minutes, resulting in total loading time. For four cranes we separate all the containers in 4 sections, and choose the section with the most containers to find the total loading time. Here we assume that the restrictions of the four cranes 
-----------------------------------------------------------------------------------------------------------------------------

Potential issues

    Runtime
        -Our program has a long runtime when loading a large set of containers, which might be an issue if it was to be used in real life. The reason for the long runtime is that we iterate through every stack in every section many times for every container that is loaded. We believe that to decrease runtime we could have stored the weights of sections and potentially stacks in different variables/lists, and just retrieved these values instead. This would have used more storage, but the main reason for why we have chosen this approach is because we believe that it makes the code easier to understand, and less complex. To our understanding optimal runtime is not the focus of this class either, and therefore we have not prioritized it.

    Testing
        -We have designed different functions in the main.py file to test the different functionalities of the program. If given the correct input, we do not see any way of this program not working as intended. In the main.py file we have made plenty of functions that test our program. To perform these tests yourself just remove the comments from each task, and it should work perfectly fine.
