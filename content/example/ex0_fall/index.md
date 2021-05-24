---
title: 自由落体
date: 2017-04-28
categories:
    - 示例
tags:
    - 挤压构造
authors:
    - 李长圣
commands:
    - start
---

{{% notice info %}}
数据下载：[fall.py](fall.py)
{{% /notice %}}

- **视频教程**：[4自由落体和Paraview颜色配置](https://www.bilibili.com/video/av91259173)

其中，`fall.py` 中内容如下：
{{< include-code "fall.py" bash >}}

程序必须以START、RESTORE和LOAD开始一个计算，上面的实例是以start开始的，生成了两个颗粒，固定蓝色颗粒，红色颗粒作自由落体运动。

- 动态图如下：

<img src="fall.gif" align="left"  />
<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> 

{{% notice info %}}
软件中所涉及的参数的单位均采用国际制标准单位（即千克kg，米m，秒s，牛N，帕Pa等）。
{{% /notice %}}

- YADE手册中有一个类似的[实例](https://yade-dem.org/doc/tutorial-examples.html#bouncing-sphere)

