import numpy as np
import matplotlib as plt
import math
import pandas as pd
import itertools
from pprint import pprint
from optparse import OptionParser

def getAllItems(transactions):
    item_set = set()
    for t in transactions:
        for item in t:
            item_set.add(item)
    item_set = list(item_set)
    item_set.pop(0)
    return set(item_set)
def pruneSup(supDict,minSup):
    minSupDict = {}
    for key in supDict.keys():
        if(supDict[key] >= minSup):
            minSupDict[key] = supDict[key]
    return minSupDict
def apriori(transactions, minSup, minConf):
    #GET L1 ITEM SETS
    rules = []
    supDict = {}
    size = len(transactions)
    for t in transactions:
        for item in t:
            if isinstance(item, str):
                item = item.strip()
                if item in supDict:
                    supDict[item] += 1
                else:
                    supDict[item] = 0
    for key in supDict.keys():
        supDict[key] /= size
    supDict = dict(sorted(supDict.items(), key=lambda x: -x[1]))
    supDict = pruneSup(supDict, minSup)
    L1 = sorted(supDict.items(), key=lambda x: -x[1])
    
    return rules
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--support", dest="minSupport",
                      help="Minimum Support value 0~1", metavar="NUMBER")
    parser.add_option("-c", "--confidence", dest="minConfidence",
                      help="Minimum Confidence value 0~1", metavar="NUMBER")
    (options, args) = parser.parse_args()
    minSupport = float(options.minSupport)
    minConfidence = float(options.minConfidence)
    dataset = pd.read_csv("./Course/Market_Basket_Optimisation.csv", header=None)
    transactions = []
    rules = apriori(list(map(list,dataset.values)), minSupport, minConfidence)