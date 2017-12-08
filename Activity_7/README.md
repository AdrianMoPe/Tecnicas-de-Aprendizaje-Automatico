# Activity 7.

## Objective.

The objective of this activity is to improve our prediction from activity 6 (with the same data set). For this, we did changes and improvements in the features selection, prediction algorithms, number of neighbors, etc, as we explaned below.

## Iquitos.

We decided use Random Forest because we obtained a better prediction than KNN. To do this, we first performed cross validation analysis in order to determine the best number of estimators base on training data: 10.

Then train with training data and predict with test-data:

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/iquitosPrediction.png)
 
 ## San Juan.
 
In San Juan we have performed KNN as in activity 6 but we have increased the number of neighbors, because using cross validation analysis we determine that the best number of neighbors to our data is 24 and weights is 'distance'
 
The features used are: 'weekofyear', 'reanalysis_specific_humidity_g_per_kg', 'reanalysis_dew_point_temp_k' and 'station_avg_temp_c'. This features were selected selected based on the correlation between features and 'total_cases'.

 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/sjPrediction.png)
 
 ## Improving our result.
 
As a result of this improvements our score has been improved from 26.8486 to 25.0962.

 ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_7/Images/score.png)