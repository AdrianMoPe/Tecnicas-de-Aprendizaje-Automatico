# Activity 5.

## Step 1: Extraction of data.

In this activity we have used both data set independently. One is the one corresponding to Iquitos between 2000 and 2010 and the other is San Juan between 1990 and 2008.

Like in the other activities we remove “year, “week” and “city” but now we add “weekofyear” to the data set. Those records that were empty have been filled with the average of all the non-empty records of that feature.

## Step 2: Data visualization.

First, the heat map of the correlation matrix has been obtained to have a first view of how they are related to each other, but because it is not a decisive method we decided to use other methods to support this decision later. 

### Iquitos.

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig1.png)
 
### San Juan.

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig1.png)
 
In order to detect outliers the PCA has been displayed. As some of the data seems to be more differentiated from the others, hierarchical clustering (with the Single method because it is more sensitive to outliers) is performed in both data set and the following conclusions have been obtained:

It has been decided to consider all those elements that are not part of the main group (Red in Iquitos and Azul in San Juan) as outliers, and then they have been eliminated from the data set.

### Iquitos.

 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig2.png)
  ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig3.png)

### San Juan.

 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig2.png)
  ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig3.png)

## Step 3: Features visualization.

Also we have performed an analysis about the features in order to determine if is possible to delete some of them avoid overfiting. For this, the transposed correlation matrix has been obtained and hierarchical clustering has been performed on it, obtaining the following dendrograms and their subsequent representation in the PCA:

### Iquitos.

 ![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig4.png)
 ![(Fig 5)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig5.png)

### San Juan.

  ![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig4.png) ![(Fig 5)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig5.png)

We observe that some features are overlap, so we can delete those which are overlap, keeping one of each group as representative. In order to know which feature of each group is selected, we obtain the relevance of each one within the dataset (correlation of each one with the total_cases number), and we choose which had more correlation. In this way the remaining features are the following:

### Iquitos || San Juan.

 ![(Fig 6)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig6.png) ![(Fig 6)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig6.png)
 
Once the features have been selected we need to build a decision tree model but first we perform cross validation analysis (with range between 2 and 30) between our selected features and total cases, in order to select the best max_depth parameter for the decision tree model.
 
 ### Iquitos || San Juan.

 ![(Fig 7)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/Iquitos/Fig7.png) ![(Fig 7)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_5/Images/San%20Juan/Fig7.png)

Max_depth: 2.
  
  
## Step 4: Features selection.

With the decision tree model we obtain this relevances: 

### Iquitos.

Feature relevance:
reanalysis_air_temp_k -> 0.0901639  
reanalysis_dew_point_temp_k -> 0.106557  
reanalysis_relative_humidity_percent -> 0  
reanalysis_specific_humidity_g_per_kg -> 0.803279  

With this we can determine that "reanalysis_air_temp_k", "reanalysis_dew_point_temp_k" and "reanalysis_specific_humidity_g_per_kg" are the most relevant features to Iquitos.

### San Juan.

Feature relevance: 
weekofyear -> 0.869811  
reanalysis_air_temp_k -> 0  
reanalysis_avg_temp_k -> 0  
reanalysis_dew_point_temp_k -> 0  
reanalysis_specific_humidity_g_per_kg -> 0.130189  
station_avg_temp_c -> 0

Therefore the relevant features in this case are "weekofyear" and "reanalysis_specific_humidity_g_per_kg". In spite of the algorithm only selects two features and we think that are insufficient, based on the correlation between features and "total_cases", we have decided to select "reanalysis_dew_point_temp_k" feature too.
