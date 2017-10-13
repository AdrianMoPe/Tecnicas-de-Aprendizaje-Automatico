# -*- coding: utf-8 -*-

'''
@author: Adrian Mora Perela
@author: Sergio Grande Murillo
'''

import codecs

def loaddata(path):
    iquito = []
    features=[]  
    try:
        f = codecs.open(path, "r", "utf-8")
        count = 0
        for line in f:
            if count > 0: 
                # remove double quotes
                row = line.replace ('"', '').split(",")
                row.pop(0)
                row.pop(0)
                row.pop(0)
                row.pop(0)
                if row != []:
                    data = [float(el) for el in row]
                    iquito.append(data)
            else:
                features=line.replace('"','').split(",")[4:]
            count += 1
            
            
    finally:
        f.close()
    return iquito, features