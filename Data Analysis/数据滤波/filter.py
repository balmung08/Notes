import scipy.signal as signa
import matplotlib.pyplot as plt
import numpy as np
import pandas
import math

fig = plt.figure()
ax = fig.add_subplot(241)  # 划分为x行x列，在第x个位置绘图
ax.set(xlim=[0, 2400], ylim=[100, 400], title='data')  # 轴范围，轴标题，图标题
ax2 = fig.add_subplot(242)
ax2.set(xlim=[0, 2400], ylim=[100, 200], title='1')  # 轴范围，轴标题，图标题
ax3 = fig.add_subplot(243)
ax3.set(xlim=[0, 2400], ylim=[100, 200], title='2')  # 轴范围，轴标题，图标题
ax4 = fig.add_subplot(244)
ax4.set(xlim=[0, 2400], ylim=[100, 400], title='3')  # 轴范围，轴标题，图标题
ax5 = fig.add_subplot(245)
ax5.set(xlim=[0, 2400], ylim=[100, 400], title='4')  # 轴范围，轴标题，图标题
ax6 = fig.add_subplot(246)
ax6.set(xlim=[0, 2400], ylim=[250, 350], title='5')  # 轴范围，轴标题，图标题
ax7 = fig.add_subplot(247)
ax7.set(xlim=[0, 2400], ylim=[100, 200], title='6')  # 轴范围，轴标题，图标题
ax8 = fig.add_subplot(248)
ax8.set(xlim=[0, 2400], ylim=[100, 200], title='7')  # 轴范围，轴标题，图标题
aisles = pandas.read_excel("23.xlsx", index_col=0)
list = []
n = 0
for m in aisles.index:
    n += 1
for i in range(0, n):
    list.append(i)


# 限幅滤波法——除去骤然升降的噪点，没啥别的用
def limitingamplitude(inputs, per):
    result = []
    result.append(inputs[0])
    m = 1
    for i in range(1, n):
        if abs((inputs[m] - inputs[m - 1])) >= per:
            result.append(inputs[m - 1])
        else:
            result.append(inputs[m])
        m += 1
    return result
result = limitingamplitude(aisles.index, 5)

# 算术平均滤波法——适合对平稳信号加随机干扰滤波，平滑度较低
def ArithmeticAverage(inputs, per):
    print(inputs)
    if np.shape(inputs)[0] % per != 0:
        lengh = np.shape(inputs)[0] / per
        for x in range(int(np.shape(inputs)[0]), int(lengh + 1) * per):
            inputs = np.append(inputs, inputs[np.shape(inputs)[0] - 1])

    inputs = inputs.reshape((-1, per))
    mean = []
    for tmp in inputs:
        for i in range(0, per):
            mean.append(tmp.mean())
            if len(mean) == len(aisles.index):
                break
        if len(mean) == len(aisles.index):
            break
    return mean
result1 = ArithmeticAverage(aisles.index, 5)

# 滑动窗口滤波法——适合周期性干扰，平滑度高，不适合处理极端值噪点
def SlidingAverage(inputs, per):
    save_f = math.ceil(per / 2) - 1
    save_e = n - save_f - 1
    l = 0
    result = []
    for q in range(0, save_f + 1):
        result.append(inputs[q])
        q += 1
    for q in range(save_f + 1, save_e):
        temp = []
        for o in range(math.ceil(q-per/2),math.ceil(q+per/2)):
            temp.append(inputs[o])
        te = np.mean(temp)
        result.append(te)
    for q in range(save_e, n):
        result.append(inputs[q])
    return result
result2 = SlidingAverage(aisles.index, 20)

# 中位值滤波法——适合去极端噪点同时滤波慢过程，对快过程效果不佳
def Median(inputs,per):
    save_f = math.ceil(per / 2) - 1
    save_e = n - save_f - 1
    result= []
    for q in range(0, save_f + 1):
        temp=[]
        for l in range(0,5):
            temp.append(inputs[q+l])
        median = np.median(temp)
        result.append(median)
    for q in range(save_f + 1, save_e):
        temp = []
        for o in range(math.ceil(q-per/2),math.ceil(q+per/2)):
            temp.append(inputs[o])
        te = np.median(temp)
        result.append(te)
    for q in range(save_e, n):
        temp=[]
        for l in range(0,5):
            temp.append(inputs[q-l])
        median = np.median(temp)
        result.append(median)
    return result
result3 = Median(aisles.index,10)

# 中值平均滤波法（防脉冲干扰平均滤波法）在算术平均基础上有了防噪点功能
# 去掉最大最小值取平均
def MedianAverage(inputs,per):
    if np.shape(inputs)[0] % per != 0:
        lengh = np.shape(inputs)[0] / per
        for x in range(int(np.shape(inputs)[0]), int(lengh + 1) * per):
            inputs = np.append(inputs, inputs[np.shape(inputs)[0] - 1])
    inputs = inputs.reshape((-1, per))
    mean = []
    for tmp in inputs:
        tmp.sort()
        tmp = tmp[1:-1]
        for i in range(0, per):
            mean.append(tmp.mean())
            if len(mean) == len(aisles.index):
                break
        if len(mean) == len(aisles.index):
            break
    return mean
result4 = MedianAverage(aisles.index, 10)

# 限幅平均滤波法（限幅+滑动窗口）
def AmplitudeLimitingAverage(inputs,per,Amplitude):
    temp = limitingamplitude(inputs, Amplitude)
    result = SlidingAverage(temp,per)
    return result
result5 = AmplitudeLimitingAverage(aisles.index,10,5)

# 一阶滞后滤波法——抑制周期性干扰，用于高频场合，但相位滞后且灵敏性低
# 本次滤波结果=（1-a）*本次采样值+a*上次滤波结果
def FirstOrderLag(inputs,a):
    result = []
    result.append(inputs[0])
    for i in range(1,n):
        templast = inputs[i - 1]
        tempnow = (1-a)*inputs[i] + a*templast
        result.append(tempnow)
    return result
result6 = FirstOrderLag(aisles.index,0.5)


ax.plot(list, aisles.index, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
ax2.plot(list, result, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
#ax3.plot(list, result1, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
ax4.plot(list, result2, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
ax5.plot(list, result3, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
ax6.plot(list, result4, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸
ax7.plot(list, result5, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸v
ax8.plot(list, result6, color='r', linewidth=1, linestyle='solid', marker='.', markersize=0)  # x y 颜色 线宽 线形 标记 标记尺寸

plt.show()
