import math
import numpy as np
from itertools import islice
import copy
import networkx as nx
import matplotlib.pyplot as plt
def loadData():  # Get the distance from Deapwalk
    #f = open(filename='karate2.embeddings')
    f = open("./data/karate.csv")
    return f

def getGraph(probability):
    file  = open('./data/karate.adjlist')
    G = nx.Graph()
    lines = file.readlines()
    for line in lines:
        line_split = line.split()
        for i in range(1,len(line_split)):
            edge = []
            edge = (int(line_split[0]),int(line_split[i]))
            G.add_edge(edge,0)
    print(G.number_of_edges())
    print(G.number_of_nodes())
    nx.draw(G)
    plt.show()


def getDistance(file):
    lines = file.readlines()
    x=[]
    for line in lines:
        y = []
        line = line.split(',')
        #print(line)
        y.append(float(line[0]))
        y.append(float(line[1]))
        y.append(float(line[2]))
        x.append(y)
    distance = np.random.rand(34**2).reshape(34,34)
    distance = np.triu(distance)
    for i in range(0,34):
        for j in range(i+1,34):
            x1 = np.array([x[i][1],x[i][2]])
            x2 = np.array([x[j][1],x[j][2]])
            dis = np.linalg.norm(x1-x2)
            distance[i][j] = dis
            distance[i][i] = 0
    distance[33][33]=0
    distance += distance.T - np.diag(distance.diagonal())
    return distance

def normalization(distance): # Get the probability of propagtion by normalization

    probability = copy.deepcopy(distance)
    max_distance = probability.max()
    print(max_distance)
    min_distance_list = []
    for i in probability:
        for j in i:
            if j!=0 :
                min_distance_list.append(j)
    min_distance = min(min_distance_list)
    print(min_distance)
    for i in range(0,probability.shape[0]):
        for j in range(0,probability.shape[1]):
            if probability[i][j] == 0:
                continue
            else:
                probability[i][j] = (probability[i][j] - min_distance)/(max_distance-min_distance)
    return probability



if __name__ == '__main__':
    f = loadData()
    dis = getDistance(f)
    p = normalization(dis)
    getGraph(p)



