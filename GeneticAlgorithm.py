from NeuralClassMemory import Network
from SantaFe import SantaFeAgent



if __name__ == "__main__":

    for i in range(100):
        net = Network()
        SFA = SantaFeAgent(net)
        print(SFA.fitness())



















        
