from NeuralClassMemory import Network
from SantaFe import SantaFeAgent
from random import *

"""
if __name__ == "__main__":

    fitness=0
    maxFitness = 0
    
    while fitness<90:
        try:
            net = Network()
            SFA = SantaFeAgent(net)
            fitness = SFA.fitness()
            if fitness > maxFitness:
                maxFitness = fitness
            print(fitness)
        except KeyboardInterrupt:
            print(maxFitness)
"""
from random import *

populationSize = 20  # even number
moveLimit = 600
numberOfGenerations = 100

def instantiateAgents(populationSize):
    agents = []
    for i in range(populationSize):
        x = SantaFeAgent(Network())
        agents.append((x, x.fitness()))
    return agents


if __name__ == "__main__":

    agents = instantiateAgents(populationSize)
    
    for generation in range(numberOfGenerations):
        #print("commencing round", generation)
        agents = sorted(agents, key=lambda x: -x[1])
        #print("best score is:", agents[0][1])

        if round == numberOfGenerations-1: break
        for index in range(populationSize // 2):
            index2 = randrange(populationSize//2-1)
            if index2 >= index:
                index2 += 1
            newAgent = agents[index][0].createOffspring(agents[index2 % (populationSize//2)][0], param=numberOfGenerations/(generation+1))
            agents[index+populationSize//2] = [newAgent, newAgent.fitness()]

    print("Fitness:", agents[0][1])
    print(agents[0][0].agent.syn)
    input()













        
