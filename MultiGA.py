import math
import sys

class Location():
    def __init__(self,xloc,yloc,service, lowTime,highTime,ID):
        self.ID = ID
        self.xloc = xloc
        self.yloc = yloc
        self.service = service
        self.lowTime = lowTime
        self.highTime = highTime

#locations and time windows global

Loc0 = Location(0, 0, 2, 0, 100000000, 0)
Loc1 = Location(10, 12, 2, 2, 20, 1)
Loc2 = Location(-5, 15, 4, 2, 200, 1)
Loc3 = Location(25, -1, 5, 15, 4000, 1)
Loc4 = Location(5, 5, 3, 0, 10, 1)
Loc5 = Location(26, 4, 1, 2, 1, 1)
Loc6 = Location(-18, -9, 1, 2, 1, 1)
Loc7 = Location(10, 11, 6, 2, 1, 1)
Loc8 = Location(15, -5, 7, 2, 1, 1)
Loc9 = Location(28, 28, 2, 2, 1, 1)
Loc10 = Location(-28, 18, 1, 2, 1, 1)

def initializePop():

    initialPopulation = []

    while len(initialPopulation) < 10:

        trucks, totalDist, valid = evaluation()
        if valid == 1:
            initialPopulation

    return initialPopulation

def crossover():

def maturation():

def createPop():

def evaluation():
    trucks = 0
    totalDist = 0
    valid = 0

    return trucks, totalDist, valid
def main():

    #initialize population function

    #loop for number of generations
        #create next candidate population function


if __name__ == '__main__':
    main()