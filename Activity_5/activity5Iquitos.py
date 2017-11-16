#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Adrian Mora Perela
@autor: Sergio Grande Murillo
"""

import loaddata
import plotdata
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing 
import sklearn.neighbors
from numpy import corrcoef, transpose, arange
from scipy import cluster
import pandas as pd
from scipy.stats.stats import pearsonr 
from tabulate import tabulate
import graphviz
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import cross_val_score

    
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

# remove outliers from data
def removeOutliers(data,outliers):
    for i in outliers:
        data=data.drop(data.index[i])
        
    return data


''' ************************ '''

# load data 
data, names = loaddata.loaddata("iquitosPivot.csv")

# Correlation matrix
R = corrcoef(transpose(data))
plotdata.plotHeatMap(R,arange(0,20),range(0,20),arange(0,20),range(0,20))

# Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
datanorm = min_max_scaler.fit_transform(data)
       
# PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(datanorm)
print "Variance Ratio: ",estimator.explained_variance_ratio_

# plot XPCA
numbers = np.arange(len(X_pca))
plotdata.plotPCA(X_pca,numbers,-1.2, 1.5,-1.2, 1.5)

# Hierarchical Clustering
# Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(X_pca)
avSim = np.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# Building the Dendrogram	
clusters = cluster.hierarchy.linkage(matsim, method = 'single')
cut = 4
cluster.hierarchy.dendrogram(clusters, color_threshold=cut)
plt.title('Method: Single. Cut: %d' %cut)
plt.show()

labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters %d' % (len(set(labels)))

# Plot PCA with clusters
plotdata.plotPCAClusters(X_pca,labels,cut,-1.2,1.5,-1.2,1.5)

# Now clusters with features
features = np.transpose(data);

# Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
features_norm = min_max_scaler.fit_transform(features)

# Principal Component Analysis
estimator = PCA (n_components =2)
X_pca = estimator.fit_transform(features_norm)
print("Variance Ratio: ", estimator.explained_variance_ratio_) 

# Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(features_norm)
avSim = np.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# Building the Dendrogram	
cut=5
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')

cluster.hierarchy.dendrogram(clusters, color_threshold = cut, labels = names, leaf_rotation=90)
plt.title('Method: Complete. Cut: %d' %cut)
plt.show()

# Show the Dendrogram
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters: %d' % (len(set(labels)))
print labels
plotdata.plotPCAClusters(X_pca,labels,cut, -8,17,-0.8,4)

# load data, now we will work with pandas dataframe
f1 = pd.read_csv("iquitoPivot.csv")
f2 = pd.read_csv("iquitoLabels.csv")
data = pd.merge(f1,f2,how='right')

#delete outliers
data= removeOutliers(data,[273,244,115,104,10])

# delete features 
data= data.drop(data.columns[[0,1,3,16,13,10,4,5,6,18,22]], axis=1)

# store features name
features_name=data.columns.tolist()
features_name.pop(len(features_name)-1) #remove'total_cases' label

# correlation between features and total_cases
correlation=[]
for i in features_name:
    correlation.append(pearsonr(data[i], data['total_cases'])[0])

# plot correlation
print "Correlation:"
plotdata.plotCorr(features_name, correlation)

# Feature selection by cut value
upperCut = 0.1
lowerCut = -upperCut
selected_data, features_selected = removeFeatures(correlation, upperCut, lowerCut, features_name)

# Cross validation analysis
print "\nCross validation analysis:"
total_scores= crossVal(selected_data,features_selected)       
max_d=total_scores.index(min(total_scores))+2

# Build model
print "\nMax_depth value:",max_d
regressor = DecisionTreeRegressor(criterion='mae', max_depth=max_d, random_state=0)
regressor.fit(selected_data[features_selected], selected_data['total_cases'])

# Feature Relevances
print 'Feature Relevances:'
list1 = zip(features_selected, regressor.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

# Build .dot
dot_name='iquitosTree.dot'
dot_data = export_graphviz(regressor, out_file=dot_name, feature_names=features_selected, 
                           filled=True, rounded=True)
graph = graphviz.Source(dot_data)  
