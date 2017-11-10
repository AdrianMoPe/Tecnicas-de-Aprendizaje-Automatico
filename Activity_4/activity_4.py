#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr 
from tabulate import tabulate
import graphviz
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import cross_val_score

# Plot correlation
def plotCorr(features, correlation):
    y_pos = np.arange(len(features)) 
    plt.bar(y_pos, correlation, align='center', alpha=0.5)
    plt.xticks(y_pos, features,rotation=90)
    plt.ylabel('Correlation')
    plt.title('Correlation features vs target')
    plt.show()
    
# Cross validation analysis
def crossVal(selected_data,features_selected):
    total_scores = []
    for i in range(2, 30):
        regressor = DecisionTreeRegressor(max_depth=i)
        regressor.fit(selected_data[features_selected], selected_data['total_cases'])
        scores = -cross_val_score(regressor, selected_data[features_selected], 
                                  selected_data['total_cases'], scoring='neg_mean_absolute_error', cv=10)
        total_scores.append(scores.mean())
    
    plt.plot(range(2,30), total_scores, marker='o')
    plt.xlabel('max_depth')
    plt.ylabel('cv score')
    plt.show() 
    
    return total_scores

# Remove features by cut value
def removeFeatures(correlation, upperCut, lowerCut, features_name):
    
    erasable=[] 
    for a in range(0,len(correlation)):
        if correlation[a]<upperCut and correlation[a]>lowerCut:
            erasable.append(a)
    
    #delete features unused from data
    selected_data = data.drop(data.columns[erasable], axis=1)
    
    i=0
    features_selected=[]
    for b in range(0,len(features_name)):
        if b==erasable[i]:
           i+=1
           if i==len(erasable):
               break
        else:
           features_selected.append(features_name[b])
           
    return selected_data,features_selected
    
# load data
f1 = pd.read_csv("denguepivot.csv")
f2 = pd.read_csv("denguelabels.csv")
data = pd.merge(f1,f2,how='right')

# delete features (city, week_start_date)
data=data.drop(data.columns[[0,3]], axis=1)

# store features name
features_name=data.columns.tolist()
features_name.pop(len(features_name)-1) #remove'total_cases' label

# correlation 
correlation=[]
for i in features_name:
    correlation.append(pearsonr(data[i], data['total_cases'])[0])

# plot correlation
print "Correlation:"
plotCorr(features_name, correlation)

# Feature selection by cut value
upperCut = 0.18 
lowerCut = -upperCut
selected_data, features_selected = removeFeatures(correlation, upperCut, lowerCut, features_name)

# Cross validation analysis
print "\nCross validation analysis:"
total_scores= crossVal(selected_data,features_selected)       
max_d=total_scores.index(min(total_scores))+2

# Build model
print "\nMax_depth value:",max_d
regressor = DecisionTreeRegressor(criterion='mse', max_depth=max_d, random_state=0)
regressor.fit(selected_data[features_selected], selected_data['total_cases'])

# Feature Relevances
print 'Feature Relevances:'
list1 = zip(features_selected, regressor.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

# Build .dot
dot_name='tree.dot'
dot_data = export_graphviz(regressor, out_file=dot_name, feature_names=features_selected, 
                           filled=True, rounded=True)
graph = graphviz.Source(dot_data)  

