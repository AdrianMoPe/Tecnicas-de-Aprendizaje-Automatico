# -*- coding: utf-8 -*-
"""
    @author: Adrian Mora Perela
    @author: Sergio Grande Murillo
"""
import codecs
import csv

f = codecs.open("iquitosTest.csv", "r", "utf-8")
data = []
try:
    reader = csv.reader(f)
    readerL = list(reader) # convert iterator to list
    means=[0]*len(readerL[0]) # sets the size of the list and initiates it to 0s

    for row in readerL:
        # filters by "iquito"
        if row[0]=='iq': 
            data.append(row)  
            # add values for the mean
            for i in xrange(len(row)):
               if i>3 and row[i]!='':
                   means[i]+=float(row[i])  
finally:
    f.close()

# sets the mean in empty fields
for row in data:
    for i in range(len(row)):
        if row[i]=='':
            row[i]="{0:.10f}".format(means[i]/len(data))

# write the results in a csv file
f =codecs.open("IquitosTestPivot.csv",'wt')

try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('city','year','weekofyear','week_start_date','ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw',
                     'precipitation_amt_mm','reanalysis_air_temp_k','reanalysis_avg_temp_k','reanalysis_dew_point_temp_k',
                     'reanalysis_max_air_temp_k','reanalysis_min_air_temp_k','reanalysis_precip_amt_kg_per_m2',
                     'reanalysis_relative_humidity_percent','reanalysis_sat_precip_amt_mm','reanalysis_specific_humidity_g_per_kg',
                     'reanalysis_tdtr_k','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c',
                     'station_min_temp_c','station_precip_mm'))
    writer.writerows(data)
finally:
    f.close()