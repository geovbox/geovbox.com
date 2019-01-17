---
title: VBOX概览
date: 2017-10-28
categories:
    - 软件
authors:
    - 李长圣
images:
    - VBOX_GUI.png
slug: VBOX-overview
---

{{% notice info %}}
下载：[VBOX简介](VBOX-overview.pdf)
{{% /notice %}}

VBOX全称virtual sandbox,即虚拟沙箱软件，是一个用于构造变形研究的二维离散元（DEM）软件。2014年开发，采用C语言编写，并用OpenMP完成了并行设计，已获软件著作权。主要面向构造模拟，用来补充构造物理沙箱实验在应力应变及材料选取上的局限性，为构造变形研究提供一种新的方法。

软件与手册会逐渐完善，敬请期待！


VBOX(virtual sandbox) is a 2D DEM program to simulate the geological problems. It is developed by C-language. We takes  three years  to construct the new data structure and neighbor search algorithm based on grid for VBOX. Furthermore, GUI was embeded into VBOX using [gtkmm](https://www.gtkmm.org/) [PLplot](http://plplot.sourceforge.net/) [Cairo](https://www.cairographics.org/)


VBOX可以完成休止角试验、直剪试验、双轴试验和构造模拟试验，见下载。

VBOX桌面版一直在开发中，预览版见下图：

{{< figure src="VBOX_GUI.png" title="VBOX桌面版预览" >}}

