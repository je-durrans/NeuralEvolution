import numpy as np

#np.random.seed(1)

def nonlin(x, deriv=False):
    if deriv==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
class Network:

    def __init__(self, weights=[], history=4, hiddenNodes=10):

        self.historySize = history
        self.hiddenNodes = hiddenNodes
        if weights == []:
            self.syn = np.array([2*np.random.random((1+3*self.historySize, self.hiddenNodes)),
                        2*np.random.random((self.hiddenNodes, 3))
                        ])
        else:
            self.syn=[]
            pass#weights
        self.history=[0]*3*self.historySize
        
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
    c = Network()

    def test():
        digits = (0, 1)
        for i in range(20):
            fif = choice(digits)
            print(fif, end=": ")
            print(c.think(fif))
    test()


