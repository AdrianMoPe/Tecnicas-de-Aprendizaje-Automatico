# Activity 7.

## Objective.

The objective of this activity is to improve our prediction from activity 6 (with the same data set). For this, we did changes and improvements in the features selection, prediction algorithms, number of neighbors, etc, as we explaned below.

## Iquitos.

We decided use Random Forest because we obtained a better prediction than KNN. To do this, we first performed cross validation analysis in order to determine the best number of estimators based on training data. In this case the best number of estimators is 1800 with max_depth 3.

The features used were:
- reanalysis_air_temp_k
- reanalysis_dew_point_temp_k
- reanalysis_specific_humidity_g_per_kg
- reanalysis_relative_humidity_percent

This features were selected based on the correlation between features and 'total_cases'.

Then train with training data and predict with test-data:

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/iquitosPrediction.png)
 
 ## San Juan.
 
In San Juan we have performed KNN as in activity 6 but we have increased the number of neighbors, because using cross validation analysis we determine that the best number of neighbors to our data is 24 and weights is 'distance'
 
The features used were:
- weekofyear
- reanalysis_specific_humidity_g_per_kg
- reanalysis_dew_point_temp_k 
- station_avg_temp_c 

This features were selected based on the correlation between features and 'total_cases'.

 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/sjPrediction.png)
 
 ## Improving our result.
 
As a result of this improvements our score has been improved from 26.8486 to 25.0962.

 ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/bestScore.png)
