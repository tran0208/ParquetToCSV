
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import os 
import csv

pf = pq.read_pandas('train.parquet') 
train = pf.to_pandas() 
#train.info()
 
shift = 3 

iStart = 0
iEnd = len(train.columns) 
k = 0
for i in range(iStart,iEnd,shift):
    myStr =  str(k) + ".csv"
    k = k + 1
    js = 0 + i
    je = shift + i
    y = train.ix[:,js:je]  
    np.savetxt( myStr , y , fmt='%.2f' , delimiter = ',' , header = "phase0, phase1, phase2" , comments = '' ) 




 
#y1 = y.ix[:,0]
#y2 = y.ix[:,1] 
#y3 = y.ix[:,2] 

#plt.subplot(3, 1, 1)
#plt.plot(y1, 'o-')
#plt.xlabel('time (s)')
#plt.ylabel('y1')

#plt.subplot(3, 1, 2)
#plt.plot(y2, '.-')
#plt.xlabel('time (s)')
#plt.ylabel('y2')

#plt.subplot(3, 1, 3)
#plt.plot(y3, '.-')
#plt.xlabel('time (s)')
#plt.ylabel('y3') 
#plt.show()

  



