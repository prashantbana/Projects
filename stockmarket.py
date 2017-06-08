import random
import pylab 

class Stock(object):
    def __init__(self,price,distribution): 
        
        self.price = price  ## current price of the stock
        self.history = [price]
        self.distribution = distribution
        self.lastChange = 0 ## maps change in stock price when market bias is applied 
        
    def setPrice(self,price):
        
        self.price = price
        self.history.append(price) # appends the value of stocks to the history list of the respective stock
         
    def getPrice(self):
        
        return self.price
        
    def makeMove(self,mktBias,mo): ## mktbias is the market bias and mo is the momentum for momentum investors.(read notes for what are momentum investors). Changes the price of Stocks
        
        oldPrice = self.price
        baseMove = self.distribution() + mktBias ## mktbias assinged in line 57 and distribution is assigned on line 
        self.price = self.price * (1.00 + baseMove) ## since price of stock is dependent on the mktbias , rise in mktbias mean rise in stock values and mktbias = 0 means stock price remains same for the time
        
        ## checking if the changes in stocks are memoryless , i.e is past behavious of stocks affect the future behaviour.
       
        if mo:
            self.price = self.price + random.gauss(.25,.25) * self.lastChange 
           
            ## Gauss distribution bcoz more vlaues tend to be near the mean of x and y , also since changes in stock no longer affect the current price of the stock but is dependent upon previous rise or fall in value of the stocks , so we multiply the distribution with the last price or change in the value of the stock.
              
        if self.price < 0.01:  ## if the price of the stock is less than 0.001 than set the price to zero
            self.price = 0.0
            
        self.history.append(self.price) ## appned the new price to history list of the respective price 
        self.lastChange = self.price - oldPrice  ## lastchange = newprice - oldprice 
        
        
        
    def showHistory(self,figNum): ## function to draw and mark the graphs 
        
        pylab.figure(figNum)
        pylab.plot(self.history)
        pylab.title('Closing Price , Test' + str(figNum))
        pylab.xlabel('Day')
        pylab.ylabel('Price')    
          

        
def unitTestStock():
    
    def runSim(stks, fig, mo): # stks - stocks to simulate , fi
        
        mean = 0.0
        for s in stks:
            for d in range(numDays): ## recusivly calling the method makeMove in the class Stock
                s.makeMove(bias,mo) # this line calls the bias and momentum for every stock.    
            s.showHistory(fig) ## plots graph in showHistory after all the iterations are completed for everyday . Under For d loop line 56
            mean += s.getPrice() #  sums the values for all the stocks . Line 56 loop
        mean = mean / float(numStks)
        pylab.axhline(mean)
        
    numStks = 20
    numDays = 200
    stks1 = []
    stks2 = []
    bias = 0.01 # to check if the simulation is correct mktBias = 0 so stock values dont change overtime
    mo = True # change the value to see the effect on the market
    
    for i in range(numStks):
        
        volatility = random.uniform(0.0 , 0.2)
        d1 = lambda:random.normalvariate(0 ,volatility/2)
         
        d2 = lambda:random.uniform(-volatility,volatility)
        ## when parameters are changed from 0.0, volatility /2 to volatility , -volatility --> theres a sudden rise and then the prices fall down to zero quickly , within first 25  days
        ## parameter = (-volatility,volatility/2) --> drop in price is more uniform
        ## graphs between noramlvariate and gauss with same parameters (v , -v) show that normal variate graphs declines more slowly and becomes 0 after 115days
             
        stks1.append(Stock(100.0 , d1))
        stks2.append(Stock(100.0 , d2))

    runSim(stks1, 1, mo)
    runSim(stks2 , 2, mo)
            


            
unitTestStock()
pylab.show()            
                
                
                
                
                
                
                
                
                
                
                
