# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2018年    月   日
实现功能：绘制神经网络的激活函数图像
"""
import numpy as np

"""
1、Sigmoid函数
     Sigmoid 是使用范围最广的一类激活函数，具有指数函数形状 。正式定义为：
     f(x)=1/(1+e^(-x))
"""
x = -10:0.001:10;
# x=9;
sigmoid = 1 / (1 + np.exp(-x))
