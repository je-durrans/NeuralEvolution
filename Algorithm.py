from NeuralClassMemory import Agent
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

populationSize = 30  # even number
moveLimit = 600
numberOfGenerations = 800

def instantiateAgents(populationSize, bestFitness):
    agents = []
    for i in range(populationSize):
        x = SantaFeAgent(Agent())
        new = (x, x.fitness(bestFitness))
        agents.append(new)
        bestFitness = max(bestFitness, new[1])
    return agents, bestFitness


if __name__ == "__main__":

    print("Initialising population of:", populationSize)
    agents, bestFitness = instantiateAgents(populationSize, 0)

    for generation in range(numberOfGenerations):
        if (generation) % 100 == 0:
            print("Generations:", generation+1, "to", generation+100)
        #print("commencing round", generation)
        agents = sorted(agents, key=lambda x: -x[1])
        #print("best score is:", agents[0][1])

        if round == numberOfGenerations-1: break
        for index in range(populationSize // 2):
            index2 = randrange(populationSize//2-1)
            if index2 >= index:
                index2 += 1
            newAgent = agents[index][0].createOffspring(agents[index2 % (populationSize//2)][0], param=10/(generation+1))
            agents[index+populationSize//2] = (newAgent, newAgent.fitness(bestFitness))
            bestFitness = max(bestFitness, agents[index+populationSize//2][1])
        bestFitness = agents[0][1]
        if bestFitness == 89:
            print("Generation:", generation+1)
            break
        
    print("Fitness:", bestFitness)
    print(agents[0][0].agent.syn)
    input()













        
