import matplotlib.pyplot as plt
import numpy as np

'''
#新建绘图画板
fig = plt.figure()
#新建绘图坐标轴Axes
ax = fig.add_subplot(111)#划分为x行x列，在第x个位置绘图
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',ylabel='Y-Axis', xlabel='X-Axis')#轴范围，轴标题，图标题
plt.show()#展示图像
#通过数组形式创建多个图像
fig, axes = plt.subplots(nrows=2, ncols=2)#x行x列个图,此处新建了一个fig画板
axes[0,0].set(title='Upper Left')#给标号位置图设立坐标轴属性Axes
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')

#绘制线plot
x = np.linspace(0, 5*np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)
ax1 = fig.add_subplot(111)#划分为x行x列，在第x个位置绘图
ax1.plot(x, y_sin, color='r', linewidth=5, linestyle='solid',marker='.', markersize=6)#x y 颜色 线宽 线形 标记 标记尺寸
plt.show()
#数组传入数据绘图形式
x = np.linspace(0, 10, 200)
data_obj = {'x': x,
            'y1': 2 * x + 1,
            'y2': 3 * x + 1.2,
            'mean': 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1}
fig, ax = plt.subplots()
ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)#填充两条线之间的颜色
ax.plot('x', 'mean', color='black', data=data_obj)
plt.show()

#散点图scatter
x = np.arange(10)
y = np.random.randint(0,10,size=10)
ax = fig.add_subplot(111)#划分为x行x列，在第x个位置绘图
ax.set(xlim=[0, 10], ylim=[0, 10], title='An Example Axes',ylabel='Y-Axis', xlabel='X-Axis')#轴范围，轴标题，图标题
ax.scatter(x, y, s=5,color='red', marker='.')#s表示标记的大小
plt.show()

#柱状图axhline/axvline
np.random.seed(1)
x = np.arange(5)
y = np.random.randn(5)
fig, axes = plt.subplots(ncols=2, figsize=(10,10))#此处新建了一个fig画板，figsize用于调整宽与高
vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')
axes[0].axhline(0, color='gray', linewidth=2)#在水平方向上画线
axes[1].axvline(0, color='gray', linewidth=2)#在垂直方向上画线
plt.show()
#直方图还返回了一个列表，可用于更改图样
fig, ax = plt.subplots()
vert_bars = ax.bar(x, y, color='lightblue', align='center')
for bar, height in zip(vert_bars, y):#值小于0的列改变颜色
    if height < 0:
        bar.set(edgecolor='darkred', color='salmon', linewidth=3)
plt.show()

#直方图hist
np.random.seed(100)
n_bins = 10#直方图的条数
x = np.random.randn(1000, 2)#产生了两组x
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()#把二维矩阵的位置变成一维矩阵，如2.1/2.2变成3/4
colors = ['red', 'tan']
colors0 = ['r', 't']
ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors0)#density为1则为概率，为0则为数量
ax0.legend(prop={'size': 10})#调整标注曲线意义的框的尺寸，hist中的label为内容
ax1.hist(x, n_bins, density=True, histtype='barstacked')#histtype控制直方图样式，stacked为堆叠形式
ax2.hist(x,  histtype='barstacked', rwidth=0.9)#rwidth控制条的宽度
fig.tight_layout()#自动调整，使显示效果更好
plt.show()

#饼状图pie
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig1, (ax1, ax2) = plt.subplots(2)
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)#labels是各个块的标签
plt.axis('equal')   #该行代码使饼图长宽相等
#startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
ax2.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode,pctdistance=1.12,radius=5)#shadow好看的，没啥用
#pctdistance百分比距离圆心的距离，默认是0.6    autopct=%1.2f%%表示格式化百分比精确输出，小数点后数字表示小数位置
#radius控制饼图半径，默认值为1；explode :(每一块)离开中心距离；
plt.axis('equal')   #该行代码使饼图长宽相等
ax2.legend(labels=labels, loc='upper right')#loc表示标注的位置
plt.show()

#等高线图
fig, ax = plt.subplots(1,figsize=(10,10))
ax.set(xlim=[-5, 5], ylim=[-5, 5], title='An Example Axes',ylabel='Y-Axis', xlabel='X-Axis')#轴范围，轴标题，图标题
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)#生成网格节点（即为把x，y的点组成二维坐标）
z = xx*xx+yy*yy
ax.contour(x, y, z, 20, cmap='RdGy')#不填充,contourf填充,camp虚化
plt.show()

#修改坐标轴显示
data = [('apples', 2), ('oranges', 3), ('peaches', 1)]
fruit, value = zip(*data)
print(fruit, value)
fig, (ax1, ax2) = plt.subplots(2)
x = np.arange(1,4)
ax1.bar(x, value, align='center', color='gray')
ax2.bar(x, value, align='center', color='gray')
ax2.set(xticks=x, xticklabels=fruit)#修改x的标度：确定bar位置，然后修改bar的标注
ax2.tick_params(axis='y', direction='inout', length=10) #ticks即为延长坐标轴上的标度使便于观察
plt.show()

#图像布局
fig, axes = plt.subplots(2, 2, figsize=(9, 9))
fig.subplots_adjust(wspace=0.5, hspace=0.3,left=0.125, right=0.9,top=0.9, bottom=0.1)
#子图水平之间的间隔wspace=0.5，垂直方向上的间距hspace=0.3，左右上底 0.9表示边距为百分之10，是反的！
#fig.tight_layout() #自动调整，省事
plt.show()
#共用x，y轴
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)#share x，顾名思义

#挪动x，y轴位置
fig, ax = plt.subplots()
ax.plot([-2, 2, 3, 4], [-10, 20, 25, 5])
ax.spines['top'].set_visible(False)     #顶边界不可见
ax.xaxis.set_ticks_position('bottom')  # ticks 的位置为下方，分上下的。
ax.spines['right'].set_visible(False)   #右边界不可见
ax.yaxis.set_ticks_position('left')
# "data"
# 移动左、下边界到 (0, 0) 处相交
ax.spines['bottom'].set_position(('data', 0))#data是移动方式，0是移动到的位置
ax.spines['left'].set_position(('data', 0))
plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#数组传入数据绘图形式
x = np.linspace(0, 4, 41)
y = [934,938,938,939,941,939,931,937,934,932,930,815,810,807,806,802,798,801,799,801,798,
     1162,788,787,789,793,794,799,801,802,798,799,801,805,794,796,800,803,801,798,799]

z = [934,943,936,935,940,936,945,933,942,941,936,944,950,932,945,931,944,935,934,936,939,
     1498,1502,1500,1501,1505,1508,1505,1496,1499,1505,1509,1513,1498,1502,1496,1499,1490,1504,1498,1507,
     ]


data_obj = {'时间': x,
            '实际光强': y,
            '设定光强': z}
fig, ax = plt.subplots()
ax.set(title='光强变化图',ylabel='光强模拟单位', xlabel='时间/s')#轴范围，轴标题，图标题
l1, = ax.plot('时间', '设定光强', color='red', data=data_obj,linewidth=1)
l2, = ax.plot('时间', '实际光强', color='blue', data=data_obj,linewidth=1)
plt.legend(handles=[l1,l2],labels=['无调节光强','有调节光强'],loc='best')
ax.vlines(1,750,1550, linestyles='dashed', colors='black')
ax.vlines(2,750,1550, linestyles='dashed', colors='black')
ax.hlines(y=1500, xmin=0, xmax=2,linestyles='dashed', colors='grey')
ax.hlines(y=800, xmin=0, xmax=4,linestyles='dashed', colors='grey')
'''
l2 = ax.hlines(y=1500, xmin=0, xmax=1, colors='blue')
ax.hlines(y=1300, xmin=1, xmax=2, colors='blue')
ax.vlines(1,1300,1500, colors='blue')
ax.vlines(1,1250,1550, linestyles='dashed', colors='black')
plt.legend(handles=[l1,l2],labels=['实际光强','目标光强'],loc='best')
'''
plt.show()



