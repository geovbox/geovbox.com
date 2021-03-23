---
title: 正态分布钉板实验
date: 2021-03-23
categories:
    - 用户实例
tags:
    - 正态分布
authors:
    - 钟军
images:
    - 0.png
commands:
    - gline
slug: 20210323
---

{{% notice info %}}
脚本及数据下载：  
钉子坐标：[init_xyr.dat](init_xyr.dat)  
VBOX脚本：[normal_distribution.py](normal_distribution.py)
{{% /notice %}}



这是一个基于离散元数值模拟完成的正态分布钉板实验。    

如下图中，每一个灰点表示一颗钉子，它们彼此的距离均相等，上一层的每一颗的水平位置恰好位于下一层的两颗正中间。在钉子区域上方生成一定数量的直径小于两颗钉子之间距离的小球，在入口处向下降落。小球在钉板区域向下传播，直到落在底板内为止。许许多多同样大小的小球不断从入口处下落，只要球的数目相当大，它们在底板将堆成近似于正态的密度函数图形（即：中间高，两头低，呈左右对称的古钟型）。

## <strong>动态图</strong>
{{< figure src="normal_distribution.gif" title="" >}}


## <strong>静态过程</strong>

|       |       |        |        |
| :-----| ----: | :----: | :----: |
| {{< figure src="1.png" title=""  >}}  | {{< figure src="2.png" title=""  >}}  | {{< figure src="3.png" title=""  >}}  | {{< figure src="4.png" title=""  >}}  |
|       |       |        |        |


## VBOX脚本源码 [normal_distribution.py](normal_distribution.py)

{{< include-code "normal_distribution.py" bash >}}


