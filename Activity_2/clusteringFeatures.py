# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import matplotlib.pyplot as plt
import numpy
import loaddata
from sklearn import preprocessing 
from sklearn.decomposition import PCA
from scipy import cluster
import sklearn.neighbors

# 0. Load Data
iquito,names = loaddata.loaddata("denguepivot.csv")
features = numpy.transpose(iquito);

#1. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
features_norm = min_max_scaler.fit_transform(features)

#1.2. Principal Component Analysis
estimator = PCA (n_components =2)
X_pca = estimator.fit_transform(features_norm)
print("Variance Ratio: ", estimator.explained_variance_ratio_) 

# 2. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(features_norm)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# 3. Building the Dendrogram	
cut=4
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cluster.hierarchy.dendrogram(clusters, color_threshold = cut, labels = names, leaf_rotation=90)
plt.title('Method: Complete. Cut: %d' %cut)
plt.show()

#3.1 Show the Dendrogram
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters: %d' % (len(set(labels)))

colors = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = numpy.hstack([colors] * 20)
numbers = numpy.arange(len(X_pca))
fig, ax = plt.subplots()

#4. Show XPCA
for i in range(len(X_pca)):         
    plt.text(X_pca[i][0], X_pca[i][1], i+4, color=colors[labels[i]]) 

plt.xlim(-4, 8.5)
plt.ylim(-0.4, 1.2)
ax.grid(True)
fig.tight_layout()
plt.title('Method: Complete. Cut: %d. Criterion: Distance' %cut)
plt.show()