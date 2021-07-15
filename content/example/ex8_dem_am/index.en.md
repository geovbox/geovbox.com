---
title: Calibration of the discrete element method and modelling of shortening experiments (Data)
date: 2021-05-24
categories:
    - Paper
    - Data
    - Script
authors:
    - LI ChangSheng
slug: li2021en 
---
LI Changsheng, YIN Hongwei*, et al. (2021) Calibration of the discrete element method and modelling of shortening experiments. Front. Earth Sci. [doi: 10.3389/feart.2021.636512](https://doi.org/10.3389/feart.2021.636512)

Original Research: The discrete element method (DEM) is becoming widely accepted as an effective method of addressing tectonic problems in granular materials. It is capable of reproducing structures observed in the analogue model (AM). However, the previous experiments ...

Accepted on 05 May 2021
## 演化过程

<h5> </h5>
{{< figure src="dem_am.gif" title="" width="800px" >}}
<center><h5>单位 (cm)<br><br>构造演化过程(DEM)</h5></center>

{{< figure src="dem_and_am02.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am04.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am08.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am12.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am16.jpg" title="" width="600px" >}}
<center><h5>第一幅(AM)构造物理模拟；第二幅(DEM)离散元数值模拟；第三幅DEM变形应变图。</h5></center>

## ZDEM script: 

1. 沉积过程。[gen.py](gen.py) 中内容如下：

    {{< include-code "gen.py" bash >}}

2. 挤压过程。[push.py](push.py) 中内容如下：

    {{< include-code "push.py" bash >}}

## The quantitative method of the thrust wedge based on mesh (Data) 

{{% notice info %}}
Download：[analog model.7z](analog model.7z) 
{{% /notice %}}

The images of the analog model.



