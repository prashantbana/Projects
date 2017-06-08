# Can be used to model volatility and randomness 

import pylab
import math, random

# TOC - Transfer of Control - where the control of the program is transferred after that step
class Location(object):
## Take the co-ordinates from Field module and make the neccessary changes in location of where the drunk is currently present on the field.
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def move(self, xc, yc): 
    ## xc and yc parameters are change in current location thus adding them to the previously current location gives us the new location
        return Location(self.x + float(xc), self.y + float(yc)) ## returns the new location after the drunk has moved to a new location by xc and yc
        
    def getCords(self): ## returns the co-ordinates where the drunk is.
        return self.x , self.y
        
    def getDist(self, other): ## return the total distance between the current location(self) and other location preferably the starting point
        xDist = self.x - other.x
        yDist = self.y - other.y
        return math.sqrt(xDist**2 + yDist**2)   
        
        
class compassPt(object):
## First declare what are all the possible moves are store them in a variable .
## function - check to see if the input from the code below is present in the variable , if it is then save is as a attribute , if not raise error.
## fucntion - check to see what input has the been given from the random value - NSEW and then move some distance in the particular direction. Return the distance walked.
    
    possibles = ['N','S','E','W']
    
    def __init__(self, pt): ## here pt is a compassPt instance which will hold a value of any of the directions (N S E W) . pt is passed on line 83
        if pt in self.possibles:
            self.pt = pt   ## bindind the direction to the drunk , pt is the direction he moves in the next step 
            
        else:
            raise ValueError('in compassPt__init__')

    def move(self, dist): ## dist tells us how many steps does the drunk guy takes at one go
        
        if self.pt =='N':
            return (dist , 0) # mapping how much he moves in north(+ve X axis) direction, where distance he moves --> dist is passed as an argument and subject to change, depends on the user.
            
        elif self.pt == 'S':
            return (0 , -dist) ## since south is -ve X axis
            
        elif self.pt == 'E':
            return (0 , dist)  ## now the drunk is moving on the Y axis
            
        elif self.pt == 'W':
            return (0 , -dist)
            
        else: 
            raise ValueError('in compassPt.move')


class Field(object):
## Most important module of the program - tells us how and where does the drunk move , thus will be giving a Starting location to the Drunk.
## Calls the move function in the CompassPt class with parameters -() and gets the xc and yc - change in location
## class the Location class and updates the new location with the old location being the object on which the change of location is called.
    
    def __init__(self, drunk, loc): ## drunk is the instance of the class Drunnk which holds his name, and binds it to where he's standing in the field at any point in time
    
        self. drunk = drunk # drunk is the instance/object of Drunk Class , which holds the name of the drunk
        self.loc = loc ##  saves the location as a tuple
        
    def move(self, cp, dist): ## cp is the instance of compassPt Class which is equal to pt(line 84), maps how much distance will the drunk guy move and gives us the new co-ordinates 'xc' and 'yc'
    
        oldLoc = self.loc 
        xc , yc = cp.move(dist) ## calling method move in compassPt class and stores values ( 0 , +-1 ) or (+-1 , 0) in xc and yc , assumming dist = 1 . See TOC - 32 
        self.loc = oldLoc.move(xc , yc) ## uses oldLoc as the instance self and pass the parameters to the 'move' methods of the Location class.         
     
    def getLoc(self):
        return self.loc
        
    def getDrunk(self):
        return self.drunk
        

class Drunk(object):
## Gives a name to the drunk and then tests to see if the drunk is in the field.
## 'move' function gets a random value from EWNS and stores it in a instance of the class CompassPt
## calls the 'move' function of the field(instance of Field) and passes the parameters - instance of the CompassPt and the distance the drunk will be moving in any direction.
    
    def __init__(self,name):
        
        self.name = name 
        
    def move(self, field, time = 1): ## time = 1 is a default constant now. This method is going to define in which direction is the drunk going to move.
    
        if field.getDrunk() != self:
            raise ValueError('Drunk.move called with the drunk not in the field')
            
        for i in range(time): ## time = 1   
            
            pt = compassPt(random.choice(compassPt.possibles)) ## pt is a instance of class compassPt which holds any one value - North East West or South
            field.move(pt , 1) ## here the value of the distance moved is 1 , for method move(self, cp, dist) in the Field Class , also pt is passed as cp in the method move. TOC - Line 57
             
            
            
            
def performTrial(time,f):   ## 'time' is the number of steps the drunk guy will take, and 'f' is a instance of the field
                
    start = f.getLoc() ## gets the locaton passed in the argument of Field Class instance
    distances = [0.0] ## list we are going to use to store how the drunk guy will move with every step
    
    for t in range(1 , time+1): ## this step will be repeated for time = 'time' passed as the argument
        
        f.getDrunk().move(f) 
        
        newLoc = f.getLoc() ## f.getLoc() returns the location after the drunk guy has moved (xc , yc) on the Field
        distance = newLoc.getDist(start) # here newLoc is the self for 'getDist' method in 'Location' class
        distances.append(distance)
        
    return distances


def performSim(time,numTrials): ## this code will perform a number of simulation(numTrials)
    
    distLists = [] ## list of distances lists
    for trial in range(numTrials):
        
        d = Drunk('Drunk' + str(trial))
        f = Field(d , Location(0 , 0))
        distances = performTrial(time , f ) ## returns a list of distances
        distLists.append(distances)
        
    return distLists
    
def ansQuest(maxTime , numTrials): ## this is the interactive mode . Here we are doing more than 1 walks and then we are calculating data to give us the average distance traveled in the time specified.Time and the num of Trials are the parameters of ansQuest which respond to where will the drunk be after steps = time and repeat his trial for 'num of Trials ' this will help us get an average estitmate as the walk is random and we want some predicative power by studying the graph

    means = []
    distLists = performSim(maxTime, numTrials)
    
    for t in range(maxTime + 1):
        tot = 0.0 ##    
        
        for distL in distLists:
            tot += distL[t] #total of distances of each list in distLists
            
        means.append(tot / len(distLists))
        
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('Distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs Time' + (str(len(distLists)) + 'trials'))

ansQuest(500 , 100) ## here time = 500 and the numTrials per walks is 300 . 
pylab.show()
               
        
