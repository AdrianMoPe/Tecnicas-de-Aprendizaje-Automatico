# Activity 4.

## Step 1: Extraction of data.

In this activity we work with the data which belongs to Iquitos since 2008 to 2010, obtained in activity 1. This time will be used “year” and “weekofyear” features too.

A new feature is added to the data-set: total_cases, which represent the number of total cases of each week.

## Step 2: Correlation and feature Selection.

Once we have all data, we study the correlation between features and total cases:

 ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_4/Images/Fig1.png)  
As we can see, the correlation of our data is low and is delimited between 0.2 and -0.25, because of this we have decided that the relevant features in this case will be the closest to these two values, for that reason we set a cut-off value of 0.18 and -0.18.     
With this cut-off  we select the following features: year, precipitation_amt_mm, reanalysis_air_temp_k, reanalysis_avg_temp_k, reanalysis_min_air_temp_k and reanalysis_sat_precip_amt_mm.
## Step 3: Cross validation analysis.  
Once the features have been selected, we perform cross validation analysis between our selected features and total cases, in order to select the best max_depth parameter, with range between 2 and 30.  
 ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_4/Images/Fig2.png)
 
 As it is observed the value 2 is the best value, because it obtains the lowest cv score, whereby we avoid to have overfitting in our model. 


## Step 4: Build a decision tree mode.
We build our decision tree mode with max depth value of 2 and obtain the tree:

 ![(Fig 3)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_4/Images/tree.png) 
  
And the features relevances:  

- year: 0.40118  
- precipitation_amt_mm: 0.157582  
- reanalysis_air_temp_k: 0.441238  
- reanalysis_avg_temp_k: 0  
- reanalysis_min_air_temp_k: 0  
- reanalysis_sat_precip_amt_mm: 0  
 


  
