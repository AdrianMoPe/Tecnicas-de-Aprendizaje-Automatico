#!/usr/bin/env python
# -*- coding: utf-8 -*-

import loaddata
import plotdata
import numpy as np
from sklearn import metrics
from sklearn import preprocessing
from sklearn.cluster import KMeans 

# Load data 
data, features = loaddata.loaddata("denguepivot.csv")
labels = [0 for x in range(len(data))]

''' *** HAY QUE QUITAR OUTLIERS *** '''
#esto deberia hacerse en el loaddata

#data.pop(124)
#data.pop(98)
#data.pop(52)
#data.pop(19)

# normalization
min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(data)

# plot 
plotdata.showdata(data,['blue'],"titulo",-0.2,1.2,-0.2,1.2) 

init = 'k-means++' # initialization method 
#init = 'random' # initialization method 
iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 # random

### 5. Find the best value for k
silhouettes = []
distortions=[]
rangeK=range(2,11)

for i in rangeK:
    km = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
    labels = km.fit_predict(data)
    distortions.append(km.inertia_)
    silhouettes.append(metrics.silhouette_score(data, labels))

# Plot distoritions  
plotdata.showSilDis(rangeK,distortions,'Number of clusters','Distortion')

# Plot Silhouette
plotdata.showSilDis(rangeK,silhouettes,'Number of clusters','Silhouette')

# 5.1 Select the best value for k
k= rangeK[silhouettes.index(np.amax(silhouettes))] #obtine el silouettes mayor, su indice, y coge el valor de rangeK asociado

# 3. Clustering execution
print("Selected K: %.f" % k)
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
y_km = km.fit_predict(data)

# 3. Validation
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(data, y_km))  
print('Distortion: %.2f' % km.inertia_)

#4 . Visualization
plotdata.showdata(data,y_km,"titulo",-0.2,1.2,-0.2,1.2)





