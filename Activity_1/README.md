# Activity 1. Principal Component  Analysis

## Step 1: Extraction of data 

  To start with the problem we make a data filter to obtain the set of assigned data, in this case we want to select data between 2008 and 2010 belonging to Iquito.
  
  We have decided to obtain the data from the original file and create a new file with our range of data. These data are going to be used to obtain the data correlation and the PCA. 
  Some rows contains empty values, for this reason we inserted the average of that column of the data set in this empty fields.
  
  Finally we decided that the first 4 columns are only to identifier each row, so that they are not important in order to obtain Correlation or PCA, for this reason we didn’t use this features.


## Step 2: Extract the correlations among features

  We obtain the correlation matrix:
  
   ![(Fig 1)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_1/Fig1.png)
  
  
  Then we can observe that the features corresponding with the columns: 0,1,2 and 3 are correlating (Must be remembered that we didn’t take first 4 columns, so that this features are: 4,5,6 and 7 in original datata set). 
  
  0(4).ndvi_se –  Pixel southeast of city centroid.
  
  1(5).ndvi_sw – Pixel southwest of city centroid.
  
  2(6).ndvi_ne –  Pixel northeast of city centroid.
  
  3(7).ndvi_nw – Pixel northwest of city centroid.
  
 Also we observe one correlation of 0.982694 betwenn features 5(9) and 6(10):
 
  5(9).reanalysis_air_temp_k -  Mean air temperature.
  
  6(10).reanalysis_avg_temp_k - Average air temperature.
  
 And finally one correlation between 4(8) and 12(16), whose correlation coefficient is 1, this mean that we can delete one of these features without repercussion in our posterior analysis. 
 
  4(8).precipitation_amt_mm - Total precipitation .
  
  12(16).reanalysis_sat_precip_amt - Total precipitation.
  

## Step 3: Execute PCA

  We obtaion the Principal Component Analysis of data set:
  
  ![(Fig 2)](https://github.com/AdrianMoPe/Tecnicas-de-Aprendizaje-Automatico/blob/master/Activity_1/Fig2.png)
  
  Here we have one outliner the row 124 and, maybe, the row 19.
 
