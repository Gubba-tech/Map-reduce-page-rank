#! /gpfs/software/Anaconda2/bin/python
import numpy as np
import pandas as pd

M = pd.read_csv("/gpfs/projects/AMS598/projects/project2/project2_data.csv",header = None)
V = pd.read_csv("/gpfs/home/weicdeng/project/hw2/v3.csv")

V.columns = ['useless','row','value.v', 'colum']
del V['useless']
M.columns = ['colum','row']
n = 10000000
a = pd.DataFrame(np.arange(1,n+1))
b = pd.DataFrame(np.ones(n))
M['count'] = np.ones(len(M))
value = 1/M.groupby('colum').sum()
value.columns = ['rowadd','count']
value['colum'] = value.index
M.columns = ['colum','row','value']
M1 = pd.merge(M,value,on='colum',how='inner')
M1 = M1.drop(['value','rowadd'],axis=1)
M1 =  M1.loc[(M1['row'] >= 1) & (M1['row'] <= 2000000)]
V1 = pd.merge(M1,V,left_on='colum',right_on='row',how='inner')
V1['value'] = V1['count']*V1['value.v']
V1 = V1.groupby('row_x').sum()
V1 = V1.drop(['colum_x','count','row_y','colum_y','value.v'],axis=1)
V1['colum'] = np.ones(len(V1))
V1['value'] = 0.9*V1['value']+0.1*1/n
V1.to_csv('/gpfs/home/weicdeng/project/hw2/v4_1.csv')
