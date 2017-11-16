# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import pcolor, show, colorbar, xticks, yticks

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
    
def plotCorr(features, correlation):
    y_pos = np.arange(len(features)) 
    plt.bar(y_pos, correlation, align='center', alpha=0.5)
    plt.xticks(y_pos, features,rotation=90)
    plt.ylabel('Correlation')
    plt.title('Correlation features vs target')
    plt.show()
    
def plotPCA(pca,name,xm,xM,ym,yM):
    fig, ax = plt.subplots()
    for i in range(len(pca)):
        plt.text(pca[i][0], pca[i][1], name[i])  
    plt.xlim(xm, xM) 
    plt.ylim(ym, yM) 
    ax.grid(True)
    fig.tight_layout()
    plt.show()
    
def plotHeatMap(R,lx,LX,ly,LY):
    pd.set_option('expand_frame_repr', False)
    pcolor(R)
    colorbar()
    yticks(lx,LX)
    xticks(ly,LY)
    show()
    
def plotPCAClusters(pca,labels,cut,xm,xM,ym,yM):
    colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors = np.hstack([colors] * 20)
    numbers = np.arange(len(pca))
    fig, ax = plt.subplots()

    for i in range(len(pca)):
        plt.text(pca[i][0], pca[i][1], numbers[i]+4, color=colors[labels[i]]) 
    
    plt.xlim(xm, xM)
    plt.ylim(ym, yM)
    ax.grid(True)
    fig.tight_layout()
    plt.title('Method: Single. Cut: %d. Criterion: Distance' %cut)
    plt.show()
