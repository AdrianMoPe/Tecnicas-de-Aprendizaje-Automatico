# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import matplotlib.pyplot as plt

def showdata(data,labels,name,xm,xM,ym,yM):
    fig, ax = plt.subplots()
    plt.scatter(data[:,0], data[:,1], c=labels,s=75)     
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.xlim(xm, xM)
    plt.ylim(ym, yM)
    
    plt.show()
    

def showSilDis(rangeData,data,xLabel,yLabel):
    fig, ax = plt.subplots()
    ax.grid(True)
    plt.plot(rangeData, data , marker='x')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()