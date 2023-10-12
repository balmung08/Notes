import numpy as np
'''
array = np.array([[1,2,3],
                  [4,5,6]])
print(array)
print(array.ndim)#矩阵维数-二维
print(array.shape)#x行x列
print(array.size)#元素数量

#创建array数组/矩阵
a = np.array([[1,2,3],
             [4,5,6]],dtype=np.int32)#dtype表示数组内容数据格式int32/int64/float
print(a.dtype)
b = np.zeros((3,4))#全为0的矩阵，x行x列 ones全为1
print(b,b.dtype)
c = np.arange(12)
print(c)
c_martrix = np.arange(12).reshape(3,4)
print(c_martrix)
c_line = np.linspace(0,10,20).reshape(4,5)
print(c_line)

#数组的计算
#两个矩阵shape相同时可以直接加减乘除，结果是依次计算
#**表示次方，sincos需要写np.sin
print(c_line<3,"\n",c_line==3)
#矩阵的乘法是c=np.dot(a,b),是线性代数的矩阵乘法
a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.sum(a,axis=1))#axis为每一行操作
print(np.max(a,axis=0))#axis0为每一列操作
print(np.min(a))
print(np.argmin(a))#索引最小值的标号位（一维）
print(np.argmax(a))#索引最大值的标号位（一维）
print(np.average(a),np.mean(a))#求矩阵平均值
print(np.median(a))#输出中位数
print(np.cumsum(a))#输出逐个累加的矩阵
print(np.diff(a))#输出相邻的两个数的差
print(np.nonzero(a))#输出非0元素的行/列数
print(np.sort(a))#逐行升序排序
print(np.transpose)#求矩阵的转置 a.T也可以表示转置
print(np.clip(a,1,2))#限幅，大于2的元素等于2，小于1的等于1

#矩阵的检索
A = np.arange(3,15)
print(A[3])
B = np.arange(3,15).reshape(3,4)
print(B)
print(B[0],B[1][1],B[1,1])
print(B[2:3,1])#冒号表示前后之间所有的行/列，前开后闭。可不写前后，则表示到矩阵的边界
for row in B:#输出每一行，只能输出行
    print(row)
for column in B.T:#输出每一列：本来没有每一列，但是输出转置的行就是输出列
    print(column)
for item in B.flat:#把矩阵转成数据包格式
    print(item)
print(B.flatten())#把矩阵元素转成数组

#array的合并
A = np.array([1,1,1])
B = np.array([2,2,2])
#合并数组为矩阵
C = np.vstack((A,B))#上下拼
D = np.hstack((A,B))#左右拼
print(C)
print(D)
print(A.shape,C.shape)
print(A[np.newaxis,:])#给行加一个维度，横着的
print(A[:,np.newaxis])#给列加维度，变成竖着的
E = np.concatenate((A,B,B,A),axis=0)#左右，1为上下
print(E)

#矩阵的分割
A = np.arange(3,15).reshape(3,4)
print(np.split(A,2,axis=1))#将列分为等分的两块
print(np.split(A,3,axis=0))#行等分，必须能够整除才行
print(np.array_split(A,2,axis=0))#等分，但不要求整除，可以分出不同行数
print(np.hsplit(A,2))#等于np.split(A,2,axis=1)
print(np.vsplit(A,3))#等于np.split(A,3,axis=0)

#矩阵的复制
A = np.arange(3,15)
B = A
A[0]=111
print(B)#相当于把A的整个值给B。改A时B也会改变（关联）
C = np.arange(3,15)
D = C.copy()
C[0]=111
print(D)#copy仅给值，不关联。改C时D不会改变
'''