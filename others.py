# -*- coding: UTF-8 -*-
import sys,getopt
import copy
import networkx as nx
import itertools
import math
import  random
'''
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except:getopt.error
    for opt,arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
'''
def linear_threshold(g,seeds,steps=0):
    DG = copy.deepcopy(g)
    for n in DG.nodes():
        




if __name__ == '__main__':
    print("LT model")







