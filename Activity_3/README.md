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

## Step 3: Execute clustering.

Although KMeans algorithm is applied to our normalized data set, we use PCA to represent graphically our data in order to see more clearly the 3 groups.  
 ![(Fig 4)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_3/Images/Fig4.png)


Our 129 elements are distributed in this way:

Group 0 , Total: 20.  
   - Members: [1, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 52, 75, 76, 79, 81, 82, 104, 126, 127]

Group 1 , Total: 65.  
  - Members: [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 24, 36, 42, 43, 46, 47, 48, 50, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 77, 78, 80, 102, 103, 106, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 122, 123, 125]

Group 2 , Total: 44.   
  - Members: [0, 5, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 44, 45, 49, 51, 72, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 105, 107, 111, 117, 121, 124, 128]

And their mean values are:

Group 1:
- ndvi_ne: 0.24547709408
- ndvi_nw: 0.22120350083
- ndvi_se: 0.23778904802
- ndvi_sw: 0.24285985737
- precipitation_amt_mm: 46.2219076923
- reanalysis_air_temp_k: 295.911791209
- reanalysis_avg_temp_k: 296.903697802
- reanalysis_dew_point_temp_k: 294.349173626
- reanalysis_max_air_temp_k: 304.913461538
- reanalysis_min_air_temp_k: 290.720307692
- reanalysis_precip_amt_kg_per_m2: 46.6065153846
- reanalysis_relative_humidity_percent: 92.0774131868
- reanalysis_sat_precip_amt_mm: 46.2219076923
- reanalysis_specific_humidity_g_per_kg: 16.2950032967
- reanalysis_tdtr_k: 7.89168131868
- station_avg_temp_c: 25.9245064103
- station_diur_temp_rng_c: 9.2942673077
- station_max_temp_c: 32.2409230769
- station_min_temp_c: 20.3426923077
- station_precip_mm: 28.3182307692

Group 2:
- ndvi_ne: 0.219583534
- ndvi_nw: 0.222810279385
- ndvi_se: 0.211234759231
- ndvi_sw: 0.235179647077
- precipitation_amt_mm: 83.1306153846
- reanalysis_air_temp_k: 297.667758242
- reanalysis_avg_temp_k: 298.846153846
- reanalysis_dew_point_temp_k: 296.571054945
- reanalysis_max_air_temp_k: 305.56
- reanalysis_min_air_temp_k: 293.878461538
- reanalysis_precip_amt_kg_per_m2: 95.9596923077
- reanalysis_relative_humidity_percent: 94.4913626374
- reanalysis_sat_precip_amt_mm: 83.1306153846
- reanalysis_specific_humidity_g_per_kg: 18.2172747253
- reanalysis_tdtr_k: 7.23384615385
- station_avg_temp_c: 27.4589605523
- station_diur_temp_rng_c: 10.2394088757
- station_max_temp_c: 33.9125680473
- station_min_temp_c: 21.5753846154
- station_precip_mm: 54.447147929

Group 3:
- ndvi_ne: 0.295778713636
- ndvi_nw: 0.285154602273
- ndvi_se: 0.288580827273
- ndvi_sw: 0.318089743182
- precipitation_amt_mm: 48.4995454545
- reanalysis_air_temp_k: 298.786461039
- reanalysis_avg_temp_k: 300.174350649
- reanalysis_dew_point_temp_k: 295.860974026
- reanalysis_max_air_temp_k: 308.795454545
- reanalysis_min_air_temp_k: 293.531818182
- reanalysis_precip_amt_kg_per_m2: 50.3520454545
- reanalysis_relative_humidity_percent: 86.3926623377
- reanalysis_sat_precip_amt_mm: 48.4995454545
- reanalysis_specific_humidity_g_per_kg: 17.4825649351
- reanalysis_tdtr_k: 10.1642857143
- station_avg_temp_c: 28.0862558275
- station_diur_temp_rng_c: 11.9635725524
- station_max_temp_c: 35.5181818182
- station_min_temp_c: 21.0568181818
- station_precip_mm: 30.9726573427

