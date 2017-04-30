import numpy as np

#np.random.seed(1)

def nonlin(x, deriv=False):
    if deriv==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
class Agent:

    def __init__(self, weights=[], history=4, hiddenNodes=10):
        self.historySize = history
        self.hiddenNodes = hiddenNodes
        if weights == []:
            self.syn = np.array([2*np.random.random((1+3*self.historySize, self.hiddenNodes))-1,
                                 2*np.random.random((self.hiddenNodes, 3))-1
                                 ])
        else:
            self.syn=weights

        self.history=[0]*3*self.historySize

    def getRandomArray(self, param=1):
        syn = np.array([2*param*np.random.random((1+3*self.historySize, self.hiddenNodes))-param,
                        2*param*np.random.random((self.hiddenNodes, 3))-param
                        ])
        return syn
    
    def think(self, foodInFront):
        
        inputData = np.array([foodInFront]+self.history)
        
        for i in range(len(self.syn)):
            inputData = nonlin(np.dot(inputData, self.syn[i]))

        output = []
        for x in inputData:
            output.append(x)
        index = output.index(max(output))
        for x in range(len(output)):
            output[x]=int(x==index)
        self.history = self.history[3:]
        for x in output:
            self.history.append(x)
        #print(output)
        if output[0]:
            return "L"
        if output[1]:
            return "F"
        if output[2]:
            return "R"
        raise ValueError("All outputs are zero")

if __name__ == "__main__":
    from random import choice
    c = Agent()

    def test():
        digits = (0, 1)
        for i in range(20):
            fif = choice(digits)
            print(fif, end=": ")
            print(c.think(fif))
    test()


