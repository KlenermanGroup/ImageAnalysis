import numpy as np
import pandas as pd
import os
import sklearn
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

print sklearn.__version__


if __name__ == '__main__':
    for i in xrange(3,4):
        pathList = []
        pathList.append(r"/Users/Mathew/Dropbox (Cambridge University)/PGA PDRA/Analysis/Mito/Tomm20/561/1/")
    
    #path1
       #pathList.append("") #path2
       #pathList.append("") #path3
        for path in pathList:
            os.chdir(path)
            fit = pd.read_table('allfitsnew.txt')
            F = np.array(zip(fit['all_XW'],fit['all_YW']))
            try:
                db = DBSCAN(eps=1.5, min_samples=20).fit(F)
                labels = db.labels_
                n_clusters_ = len(set(labels)) - (1 if-1 in labels else 0)
                print('Estimated number of clusters: %d' % n_clusters_)
                
                fit['Cluster'] = labels
                fit.to_csv(path + '/' + 'Results'+str(1.5)+'_20.csv', sep = '\t')
            except ValueError:
                pass
    
