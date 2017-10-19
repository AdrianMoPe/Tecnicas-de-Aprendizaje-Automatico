# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import loaddata
import plotdata
import numpy as np
from sklearn import metrics
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans 

# Load data 
data, features = loaddata.loaddata("denguepivot.csv")
labels = [0 for x in range(len(data))]

# Remove outlier
data.pop(124)

# Normalization
min_max_scaler = preprocessing.MinMaxScaler()
data_norm = min_max_scaler.fit_transform(data)

# PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(data_norm)
print(estimator.explained_variance_ratio_) 

# plot PCA
plotdata.showdata(X_pca,['green'],"PCA",-1.2,1.4,-1.2,1.4) 

# Set kmeans parameters
init = 'k-means++' # initialization method 
#init = 'random' # initialization method 
iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 

# Find the best value for k
silhouettes = []
distortions=[]
rangeK=range(2,11)
labels = [0 for x in range(len(data_norm))]

for i in rangeK:
    kmeans = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
    labels = kmeans.fit_predict(data_norm)
    distortions.append(kmeans.inertia_)
    silhouettes.append(metrics.silhouette_score(data_norm, labels))

# Plot distoritions  
plotdata.showSilDis(rangeK,distortions,'Number of clusters','Distortion')

# Plot Silhouette
plotdata.showSilDis(rangeK,silhouettes,'Number of clusters','Silhouette')

# Select the best value for k
k= rangeK[silhouettes.index(np.amax(silhouettes))] 

# Clustering execution
print("Selected K: %.f" % k)
kmeans = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels = kmeans.fit_predict(data_norm)

# Validation
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(data_norm, labels))  
print('Distortion: %.2f' % kmeans.inertia_)

# Visualization
plotdata.showdata(X_pca,labels,"k-means++",-1.2,1.4,-1.2,1.4)

# Show the elements which belong to each group
for c in range(0,k):
    grupos=[]
    for i in range(len(data)): 
        if labels[i]==c:
            grupos.append(i)

    print '\nGroup', c,", Total: ",len(grupos)
    print '   Members:',grupos
    
# Show the means of each group
for c in range(0,k):
    s=''
    print '\nGroup',c+1
    for i in range(len(data[0])):
        column=[row[i]for j, row in enumerate(data) if labels[j]==c]
        if len(column)!=0:
            print "-",features[i],":", np.mean(column)
        




