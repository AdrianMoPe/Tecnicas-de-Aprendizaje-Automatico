# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''
import loaddata
from sklearn import preprocessing 
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sklearn.neighbors
import numpy
from scipy import cluster

# Load data 
data, features = loaddata.loaddata("denguepivot.csv")

# Data normalizazion
min_max_scaler = preprocessing.MinMaxScaler()
datanorm = min_max_scaler.fit_transform(data)

# Principal Component Analysis
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(datanorm)
print("Variance Ratio: ", estimator.explained_variance_ratio_) 

# Hierarchical Clustering
# Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(X_pca)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# Building the Dendrogram	
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cut = 6 
cluster.hierarchy.dendrogram(clusters, color_threshold=cut)
plt.title('Method: Complete. Cut: %d' %cut)
plt.show()
 
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters %d' % (len(set(labels)))

# Plot PCA
colors = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = numpy.hstack([colors] * 20)
numbers = numpy.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i], color=colors[labels[i]]) 

plt.xlim(-1.2, 1.5)
plt.ylim(-1.2, 1.5)
ax.grid(True)
fig.tight_layout()
plt.title('Method: Complete. Cut: %d. Criterion: Distance' %cut)
plt.show()

# Characterization
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)

# Show Groups
for c in range(1,n_clusters_+1):
    print 'Group', c
    for i in range(len(datanorm[0])):
        column = [row[i] for j,row in enumerate(data) if labels[j] == c]
        if len(column) != 0:
            print "-",features[i],":", numpy.mean(column)


# Show the elements which belong to each group
for c in range(1,n_clusters_+1):
    grupos=[]
    for i in range(len(data)): 
        if labels[i]==c:
            grupos.append(i)

    print 'Group', c,", Total: ",len(grupos)
    print '   Members:',grupos
       
        
