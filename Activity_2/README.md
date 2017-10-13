# Activity 2.

## Step 1: Extraction of data.

In this activity we work with the data which belongs to Iquitos since 2008 to 2010, obtained from the activity 1. 
As in the activity 1, we don't use the first 4 columns. After load data the first step is normalize the data set using the MinMaxScaler 
function in order to work with it.  
  
Also we execute PCA to visualize it and view more clearly how data is grouped.
This time we will also store data set's first row, which contains the name of the different features, because we will use it later.

## Step 2: Compute the similarity matrix and execute the hierarchical clustering algorithm.

In order to obtain the similarity matrix we have used an Euclidean metric to get the distance between the elements of our data set. 
Also, in order to obtain more information we compute the mean distance between elements using the PCA, in this case is 0.79.  
  
To build the Dendogram we group data into clusters according to their distances. As  method we have used ‘complete’ because is the 
best for our data, because ‘Single’ is too sensitive with the outliers. With this we have obtained 8 groups. 

## Step3: Cut the dendrogram and characterize the obtained groups.

To generate the Dendograma and the characterization we have decide to effect the cut  over 6, because is the best level that adapts
to our data. 

Results:

![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_2/Images/Fig1.png)
![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_2/Images/Fig2.png)

Our 130 elements are distributed in this way:

Group 1, Total:  21.  
Members: [3, 6, 7, 8, 10, 11, 12, 16, 17, 21, 24, 54, 62, 63, 65, 67, 68, 73, 74, 103, 123]    
Group 2, Total:  16.  
Members: [1, 18, 20, 22, 25, 28, 29, 55, 76, 78, 79, 80, 81, 82, 127, 128]  
Group 3, Total:  38.  
Members: [2, 4, 9, 13, 14, 15, 36, 42, 43, 46, 47, 48, 50, 53, 56, 57, 58, 59, 60, 61, 64, 66, 69, 70, 71, 77, 102, 106, 108, 109, 
   110, 113, 114, 116, 119, 120, 122, 126]     
Group 4, Total:  3.  
Members: [112, 115, 118]  
Group 5, Total:  26.  
Members: [30, 31, 32, 37, 38, 41, 44, 45, 49, 51, 72, 86, 87, 91, 92, 94, 95, 99, 100, 101, 107, 111, 117, 121, 125, 129]  
Group 6, Total:  8.  
Members: [19, 23, 26, 27, 52, 75, 104, 124]  
Group 7, Total:  5.  
Members: [33, 39, 88, 89, 98]  
Group 8, Total:  13.  
Members: [0, 5, 34, 35, 40, 83, 84, 85, 90, 93, 96, 97, 105]    
   
Running clusteringElements.py can be seen the mean values of the features from each group. With this mean values we have created a .xls
file in order to realise the differences between clusters:

- Cluster 1: highest values of ‘station_precip_mm’ features.
- Cluster 2: every values are normal.
- Cluster 3: values of  ‘station_precip_mm’, ‘precipitation_amt_mm’ and ‘reanalysis_precip_amt_kg_per_m2’ features higher than average.
- Cluster 4: very high values of ‘reanalysis_precip_amt_kg_per_m2’ and ‘precipitation_amt_mm’ features.
- Cluster 5: every values are normal.
- Cluster 6: low values of ‘station_precip_mm’ and ‘precipitation_amt_mm’ features.
- Cluster 7:  it’s similar to cluster 6, except ‘ndvi_sw’ feature which stands out for it’s high values.
- Cluster 8: lowest values of ‘reanalysis_precip_amt_kg_per_m2’ feature.
   
## Step 4: Execute the hierarchical clustering algorithm using feature as elements.

In this step we obtain the transposed matrix to work with the features like it was elements. This time the cut is realized over 4.

![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_2/Images/Fig3.png)
![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_2/Images/Fig4.png)

As we can see, it's obtained 5 groups. We highlight that green group is different from the others, that's because the features in this
clusters contain high values measured in Kelvin degrees and all are similar. The same happens with the yellow group, that matches with 
precipitation features measured in mm. Finally we observe that red and blue groups are similar (their values are similar).

