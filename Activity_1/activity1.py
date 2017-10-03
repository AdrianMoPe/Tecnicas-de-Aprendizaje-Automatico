# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import csv
import codecs
from pylab import pcolor, show, colorbar, xticks, yticks
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing 
from numpy import corrcoef, transpose, arange
from pylab import pcolor, show, colorbar, xticks, yticks
import seaborn as sns
from pandas import *

''' 
'''

# --- LOAD THE DATA ---
f = codecs.open("train.csv", "r", "utf-8")
iquito = []
try:
    reader = csv.reader(f)
    readerL = list(reader) # convert iterator to list
    medias=[0]*len(readerL[0]) # sets the size of the list and initiates it to 0s

    for row in readerL:
        # filters by "iquito" and between 2008 and 2010 
        if row[0]=='iq' and (int(row[1])>=2008 and int(row[1])<=2010): 
            iquito.append(row)  
            # add values for the mean
            for i in xrange(len(row)):
               if i>3 and row[i]!='':
                   medias[i]+=float(row[i])  
finally:
    f.close()

# sets the mean in empty fields
for row in iquito:
    for i in range(len(row)):
        if row[i]=='':
            row[i]="{0:.10f}".format(medias[i]/len(iquito))

# write the results in a csv file
f =codecs.open("denguepivot.csv",'wt')

try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('city','year','weekofyear','week_start_date','ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw',
                     'precipitation_amt_mm','reanalysis_air_temp_k','reanalysis_avg_temp_k','reanalysis_dew_point_temp_k',
                     'reanalysis_max_air_temp_k','reanalysis_min_air_temp_k','reanalysis_precip_amt_kg_per_m2',
                     'reanalysis_relative_humidity_percent','reanalysis_sat_precip_amt_mm','reanalysis_specific_humidity_g_per_kg',
                     'reanalysis_tdtr_k','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c',
                     'station_min_temp_c','station_precip_mm'))
    writer.writerows(iquito)
finally:
    f.close()


#--- CORRELATION  --- 
    
# Load Data
iquitoCorr = []
for line in iquito:
    row=line[4:]
    if row != []:
        iquitoCorr.append(map(float, row))
 
# plotting the correlation matrix
#http://glowingpython.blogspot.com.es/2012/10/visualizing-correlation-matrices.html
R = corrcoef(transpose(iquitoCorr))

pandas.set_option('expand_frame_repr', False)
print pandas.DataFrame(transpose(R))


pcolor(R)
colorbar()
yticks(arange(0,20),range(0,20))
xticks(arange(0,20),range(0,20))

show()

# http://stanford.edu/~mwaskom/software/seaborn/examples/many_pairwise_correlations.html
# Generate a mask for the upper triangle
sns.set(style="white")
mask = np.zeros_like(R, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(200, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(R, mask=mask, cmap=cmap, vmax=.8,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

# --- PRINCIPAL COMPONENT ANALYSIS (PCA) ---
iquitoPCA = []
for line in iquito:
    row=line[4:]
    if row != []:
        data = [float(el) for el in row]
        iquitoPCA.append(data)
     
#1. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
iquitoPCA = min_max_scaler.fit_transform(iquitoPCA)
       
#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(iquitoPCA)

print(estimator.explained_variance_ratio_) 

#3.  plot 
numbers = np.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i])  
plt.xlim(-1.2, 2) 
plt.ylim(-1.2, 1.5) 
ax.grid(True)
fig.tight_layout()
plt.show()







