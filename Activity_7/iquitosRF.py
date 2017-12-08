# -*- coding: utf-8 -*-
"""
    @author: Adrian Mora Perela
    @author: Sergio Grande Murillo
"""

from sklearn.metrics import mean_absolute_error
from tabulate import tabulate
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import csv

# load training data
f1 = pd.read_csv("iquitosPivot.csv")
f2 = pd.read_csv("iquitosLabels.csv")
data = pd.merge(f1,f2,how='right')

# delete outliers
outliers=[273,244,115,104,10]
for i in outliers:
    data=data.drop(data.index[i])

featuresName=['reanalysis_air_temp_k','reanalysis_dew_point_temp_k','reanalysis_specific_humidity_g_per_kg','reanalysis_relative_humidity_percent']

trainingData = data[featuresName]
objective = data['total_cases']

# cross validation in order to obtain the best number of estimators
print 'Performing cross validation analysis to obtain the number of estimators...'
estimators = range(1200,2000,200)

total_scores = []
for i in estimators:
    regressor = RandomForestRegressor(n_estimators= i, max_depth=3, criterion='mae', random_state=0)
    regressor.fit(trainingData, objective)
    y=regressor.predict(trainingData)
    total_scores.append(mean_absolute_error(objective,y))

estim = estimators[total_scores.index(np.amin(total_scores))]

print 'The best number of estimators is', estim, 'because he has the lowest mae'


# load test data
datosT = pd.read_csv("iquitosTestPivot.csv")
datosTest = datosT[featuresName]

# Model Parametrization 
regressor = RandomForestRegressor(n_estimators= estim, max_depth = 3, criterion='mae', random_state=0)
# Model construction
regressor.fit(trainingData, objective)
# Model prediction
print '\nPrediction:'
predictedObjective = regressor.predict(datosTest)

# Show prediction
xx = np.stack(i for i in range(len(predictedObjective)))
plt.plot(xx, predictedObjective, c='g', label='Prediction')
plt.axis('tight')
plt.legend()
plt.title("Random Forest")
plt.show()

# Features relevancies
print 'Feature Relevancies'
list1 = zip(featuresName, regressor.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

# write the results in a csv file
f =codecs.open("iquitosRFResults.csv",'wt')
data2=[]

for j in range(0,len(datosTest)):
    row=[]
    row.append(datosT.iloc[j]['city'])
    row.append(datosT.iloc[j]['year'])
    row.append(datosT.iloc[j]['weekofyear'])
    row.append(int(predictedObjective[j]))
    data2.append(row)

try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('city','year','weekofyear','total_cases'))
    writer.writerows(data2)
finally:
    f.close()
    
print '\nPrediction results are in the iquitosRF.csv file.'