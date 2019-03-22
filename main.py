# -*- coding: UTF-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import copy

def getDistance():
    f = open('./data/karate.csv')
    lines = f.readlines()
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
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            x1 = np.array([x[i][1],x[i][2]])
            x2 = np.array([x[j][1],x[j][2]])
            dis = np.linalg.norm(x1 - x2)
            distance[i][j] = dis
            distance[i][i] = 0
    distance[33][33] = 0
    return distance
def normalization(distance): # Get the probability of propagtion by normalization

    probability = copy.deepcopy(distance)
    max_distance = probability.max()
    min_distance_list = []
    for i in probability:
        for j in i:
            if j!=0 :
                min_distance_list.append(j)
    min_distance = min(min_distance_list)
    for i in range(0,probability.shape[0]):
        for j in range(0,probability.shape[1]):
            if probability[i][j] == 0:
                continue
            else:
                probability[i][j] = (probability[i][j] - min_distance)/(max_distance-min_distance)
    return probability
def getGraph(distance):
    '''
    file1 = open('./data/p.txt', 'w')
    for i in range(0,len(distance)):
        for j in range(0,len(distance)):
            if i==j:
                continue
            elif distance[i][j]==0:
                continue
            file1.write(str(str(i+1)+' '+str(j+1)+' '+str(distance[i][j]))+'\n')
   '''
    file1 = open('./data/p.txt')
    file2 = open('./data/Kgraph')
    G = nx.Graph()
    lines = file2.readlines()
    G = nx.Graph()
    edge_list = []
    for line in lines:
        edge = line.strip().split('\t')
        edge_weight = tuple([int(edge[0]),int(edge[1]),float(edge[2])])
        edge_list.append(edge_weight)
    G.add_weighted_edges_from(edge_list)
    return G


def fitness(seed, g):
    #p = 0.01
    k = len(seed)
    chrom = copy.copy(seed)
    chromTotalNei = []
    p = 0.01
    for j in chrom:
        chromTotalNei.extend(g.neighbors(j))
    NS = list(set(chromTotalNei) - set(chrom))
    fitness = 0
    for i in NS:
        rv = len(set(g.neighbors(i)) & set(chrom))
        fitness += 1 - (1 - p) ** rv
    return fitness + k
def IC_model(a,G):  # a: the set of initial active nodes
    A = set(a)  # A: the set of active nodes, initially a
    B = set(a)  # B: the set of nodes activated in the last completed iteration
    converged = False
    while not converged:
        nextB = set()
        for n in B:
            for m in set(G.neighbors(n)) - A:
                prob = random.random()  # in the range [0.0, 1.0)
                if prob <= list(G.get_edge_data(2,1).values())[0]:
                    nextB.add(m)
        B = set(nextB)
        if not B:
            converged = True
        A |= B
    return A

def random_select(G,seed_size):
    seed = random.sample(G.nodes(),seed_size)
    x = Monte_Carlo(seed,G)
    print(x)

def Monte_Carlo(seed,G):
    iteration = 10000
    su = 0.0
    for i in range(iteration):
        su += len(IC_model(seed,G))
    return su/10000


def degree_select(G,seed_size):
    seed_degree = dict(G.degree())
    seed_degree_sorted = dict(sorted(seed_degree.items(),key=lambda item:item[1],reverse=True))
    #print(seed_degree)
    sorted_nodes = seed_degree_sorted.keys()
    seed  = list(sorted_nodes)[0:seed_size]
    print(seed)
    x = Monte_Carlo(seed,G)
    print(x)


def greedy_select(g,k):
    allnodes = g.nodes()
    all_nodes = list(allnodes)
    seed_nodes = []
    for m in range(k):
        layers_activted = [] #存储每个节点激活的节点数
        length = [] #存储每个节点激活节点的个数。length = len(layers_activited)
        datas = []
        for i in all_nodes: #遍历图中的所有节点
            data = []
            data.append(i)
            datas.append(i) #？
            data_test = seed_nodes + data #将节点i放入集合seed—nodes中进行验证。














if __name__ == '__main__':
    dis = getDistance()
    dd = normalization(dis)
    G  = getGraph(dd)
    a,b =_linear_clime(G,k=5)