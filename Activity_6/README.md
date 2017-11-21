# Activity 6.

## Step 1: Extraction of data.

In this activity we have used both data set independently. One is the one corresponding to Iquitos between 2000 and 2010 and the other is San Juan between 1990 and 2008. In both data set we remove outliers.

Now we work only with the selected features in the last activity:
- Iquitos: reanalysis_air_temp_k,reanalysis_dew_point_temp_k and reanalysis_specific_humidity_g_per_kg.
- San Juan: weekofyear, reanalysis_specific_humidity_g_per_kg and reanalysis_dew_point_temp_k.

Also we need total_cases, in order to train the model, and city and year in orden to generate the result in the correct format.

## Step 2: Select the number of neighbors.

In order to select the best number of neighbors we use cross validation analysis:

### Iquitos / San juan

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/iquitosCross.png)
 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/sanJuanCross.png)

We decide take 7 neighbors for Iquitos and 9 for San Juan.

## Step 3: Build model.

When we have the number of neighbors we build the Knn model using 'uniform' and 'distance' as parameters.
The model train with our data set and we obtain:

### Iquitos

 ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/iquitosUniform.png)
 ![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/iquitosDistance.png)
 
### San Juan

 ![(Fig 5)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/sanJuanUniform.png)
 ![(Fig 6)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/sanJuanDistance.png)
 
 As we can see the best parameter is 'distance' because the prediction is better.
 
 ## Step 4: Total cases prediction.
 
 Since we have the number of neighbors (7 and 9) and the parameter (distance) we can build the knn model to predict the total cases of the test data set with our training data:
 
 ### Iquitos
  ![(Fig 7)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/iquitosPrediction.png)
 
 ### San Juan
 ![(Fig 8)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_6/images/sanJuanPrediction.png)
 
 We upload our prediction to dataDriven and our score was 26.8486
