import pandas as pd
import numpy as np
'''''
#pandas基础数据格式建立与排序
s = pd.Series([1,3,6,np.nan,5.6,9.8])
print(s)
date = pd.date_range('20210830',periods=10)
print(date)
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
print(pz)
dic = pd.DataFrame({"A":666,"b":[7,6,2]})#按字典格式定义
print(dic,dic.dtypes,"\n",dic.index,dic.columns,dic.values)
print(dic.describe())#简易数据自动分析
print(dic.T)#当作矩阵来转置
print(dic.sort_index(axis=1,ascending=False))#按列倒序排
print(dic.sort_index(axis=1,ascending=True))#正序
print(dic.sort_values(by='b',ascending=False))#按照其中一列来排序,可自定义正/倒

#pandas选择数据
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
print(pz)
print(pz['a'],pz.a)#列
print(pz[0:3])#行
print(pz.loc[[1],['a','b']])#按标签选择
print(pz.iloc[1,2])#按位置筛选
print(pz[pz<4])#按条件筛选

#给选定位置赋值
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
pz.iloc[1,2]=500#按位置改变
pz[pz<5]=0#按条件改值
#选定位置直接赋值
print(pz)

#处理丢失的数据
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
pz.iloc[1,2]=np.NAN
pz.iloc[0,1]=np.NAN
print(pz)
print(pz.dropna(axis=0,how='all'))#舍去带NaN的行，how可以写all/any，只有全是Na才舍去/只要有Na就舍去
print(pz.fillna(value=0))#填充Na为设定值
print(pz.isnull())#判断每一个位置是否有数据
print(np.any(pz.isnull())== True)#返回T则说明表格里有丢失的数据

#存取数据
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
pz.to_csv("test.csv")
test = pd.read_csv("test.csv")

#concatenating合并方式
pz = pd.DataFrame(np.arange(10).reshape(2,5),columns=['a','b','c','d','e'])
pz2 = pd.DataFrame(np.arange(12).reshape(3,4),columns=['a','b','c','d'])
res = pd.concat([pz,pz2],axis=0)#上下合并
res2 = pd.concat([pz,pz2],axis=1)#左右合并
res3 = pd.concat([pz,pz2],axis=0,ignore_index=True)#左右合并,忽略原来的列编号,重新编号
print(res)
print(res2)
print(res3)
res4 = pd.concat([pz,pz2],axis=0,join='outer')#合并，取并
print(res4)
res5 = pd.concat([pz,pz2],axis=0,join='inner',ignore_index=True)#合并，取交
print(res5)
res = pz.append(pz2, ignore_index=True)#往下加数据
#res = df1.append([df2, df3])
#一行一行的进行添加
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res = pz.append(s1, ignore_index=True)

#merge合并方式
#按照key来合并
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')
print(res)
#双key合并
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                              'key2': ['K0', 'K0', 'K0', 'K0'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on=['key1', 'key2'], how='inner') #仅考虑完全相同部分，交集
# how = ['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='left',indicator='ide')#按on中左边的作为基准,indicator是说明合并方式
print(res)
#列标注index合并
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                                  'B': ['B0', 'B1', 'B2']},
                                  index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                                     'D': ['D0', 'D2', 'D3']},
                                      index=['K0', 'K2', 'K3'])
print(left)
print(right)
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')#按列标注来考虑，并
print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')#交
print(res)
'''