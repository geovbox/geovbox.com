---
title: The first example to learn VBOX
date: 2019-01-14
categories:
    - Example
tags:
    - Push
authors:
    - LI ChangSheng
images:
    - 10km.png
commands:
    - start
---

{{% notice info %}}
数据下载：[push.py](push.py)
[演化过程图](shearSS.zip)
[init_xyr.dat](/example/ex6_palaeohigh/init_xyr.dat)
{{% /notice %}}

## 一个构造数值模拟试验的完整流程包括两个步骤：

1. 生成初始模型。生成颗粒集合体，定义颗粒的材料参数，让其在重力作用下沉积，形成初始模型。  
2. 挤压。给定墙相应的速度，开始挤压。


*这里是一个最简单的挤压计算实例，仅需30行命令。学会了该命令脚本，基本掌握VBOX的使用方法。*  
## 微观参数表

| 颗粒直径  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _d_ (m)  | 颗粒密度  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _ρ_ (kg∙m<sup>-3</sup>)   | 颗粒摩擦系数  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  | 缩短速率 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  _υ_ (m∙s<sup>-1</sup>)|  时间步 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> s |
|---------------|-----------|--------|----------|-------------|
|    60，80   |   2500   |   0.3   |   2.0   |   0.05 |

## 登陆VBOX所在集群，运行 `vboxdaily push.py` ，其中 [push.py](push.py) 中内容如下：

{{< include-code "push.py" bash >}}

{{< figure src="colorbar.png" title="" width="600px" >}}
<h5> </h5>
{{< figure src="shearSS.gif" title="" width="600px" >}}
<center><h5>单位 (km)<br><br>构造变形及应力应变的演化过程</h5></center>


{{< figure src="10km.png" title="挤压量10 km时，构造变形及应力应变" width="600px" >}}



