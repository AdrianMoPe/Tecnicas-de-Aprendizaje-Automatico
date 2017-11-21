# -*- coding: utf-8 -*-
"""
    @author: Adrian Mora Perela
    @author: Sergio Grande Murillo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import csv
from sklearn import neighbors
from sklearn.cross_validation import cross_val_score

# Load data
f1 = pd.read_csv("sanJuanPivot.csv")
f2 = pd.read_csv("sanJuanLabels.csv")
data = pd.merge(f1,f2,how='right')

# Delete outliers
data=data.drop(data.index[768])
data=data.drop(data.index[705])
data=data.drop(data.index[507])
data=data.drop(data.index[498])
data=data.drop(data.index[493])
data=data.drop(data.index[363])
data=data.drop(data.index[351])
data=data.drop(data.index[332])

# select features 
data= data[['weekofyear', 'reanalysis_specific_humidity_g_per_kg','reanalysis_dew_point_temp_k','total_cases']]
X = data[['weekofyear', 'reanalysis_specific_humidity_g_per_kg','reanalysis_dew_point_temp_k']]
y = data['total_cases']


xx = np.stack(i for i in range(len(y)))

# Cross validation analysis
for i, weights in enumerate(['uniform', 'distance']):
    total_scores = []
    for n_neighbors in range(1,30):
        knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
        knn.fit(X,y)
        scores = -cross_val_score(knn, X,y,scoring='neg_mean_absolute_error', cv=10)
        total_scores.append(scores.mean())
    
    plt.plot(range(0,len(total_scores)), total_scores, marker='o', label=weights)
    plt.ylabel('cv score')

plt.legend()
plt.show()    

# Build the model
n_neighbors = 9 #number of neighbors
for i, weights in enumerate(['uniform', 'distance']):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_pred = knn.fit(X,y).predict(X)

    plt.subplot(2, 1, i + 1)
    plt.plot(xx, y, c='k', label='data')
    plt.plot(xx, y_pred, c='g', label='prediction')
    plt.axis('tight')
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,weights))

    plt.show()


''' Prediction '''

# load data test
datosTest = pd.read_csv("SanJuanTestPivot.csv")

test = datosTest[['weekofyear', 'reanalysis_specific_humidity_g_per_kg','reanalysis_dew_point_temp_k']]

# prediction
knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
prediccion = knn.fit(X,y).predict(test)

# show prediction
print "\nPREDICTION:"
xx = np.stack(i for i in range(len(prediccion)))
plt.subplot(2, 1, i + 1)
plt.plot(xx, prediccion, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,weights))

plt.show()

# write results in a csv file
f =codecs.open("sanJuanResults.csv",'wt')
data2=[]

for j in range(0,len(datosTest)):
    row=[]
    row.append(datosTest.iloc[j]['city'])
    row.append(datosTest.iloc[j]['year'])
    row.append(datosTest.iloc[j]['weekofyear'])
    row.append(int(prediccion[j]))
    data2.append(row)

try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('city','year','weekofyear','total_cases'))
    writer.writerows(data2)
finally:
    f.close()
    