# Activity 3.

## Step 1: Extraction of data.

In this activity we work with the data which belongs to Iquitos since 2008 to 2010, obtained from the activity 1. 
As in the activity 1, we don't use the first 4 columns.   

Initially we have 130 elements but after load it the first step is remove outliers (element 124), therefore we have 129 elements, and then normalize 
the data set using the MinMaxScaler function in order to work with it.  
  
Then we execute PCA to visualize our data.

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_3/Images/Fig1.png)
 
## Step 2: Choose the number of clusters.

In order to choose the number of clusters which is better for our data set we tested the KMeans method with ‘random’ and ‘k-means++’ initialize, both with values since 2 to 10.

Based in this tests, we decided choose ‘k-means++’ and 3 clusters because it take the best Silhouette Coefficient for our data.

 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_3/Images/Fig2.png)
 ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_3/Images/Fig3.png)

To highlight, the Silhouette Coefficient is 0.22, this means that in our data set there is a lot of overlap because the value is approaching to 0.

## Step 3 :Execute clustering.

Although KMeans algorithm is applied to our normalized data set, we use PCA to represent graphically our data in order to see more clearly the 3 groups.  
 ![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_3/Images/Fig4.png)
