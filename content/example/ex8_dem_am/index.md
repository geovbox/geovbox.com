---
title: 物理模拟和数值模拟对比实验(Excellent Important Nice)
date: 2021-05-24
categories:
    - 文章
    - 脚本
authors:
    - 李长圣
images:
    - dem_and_am16.jpg
slug: ex8 
---

{{% notice info %}}
下载：
[gen.py](gen.py) |
[push.py](push.py) 
{{% /notice %}}

{{% notice note %}}
~10万颗粒，~13万时步，16核并行(Intel Xeon E5-2650)，耗时 ~**3小时** 完成计算。
{{% /notice %}}

{{< figure src="dem_am.gif" title="" width="800px" >}}
<center>单位 (cm)<br>**离散元数值模拟结果**</center>

通过休止角试验和双轴试验标定了石英砂颗粒的细观参数，构建了一个典型的构造物理模拟(AM)和离散元数值模拟(DEM)试验，对比两种方法在构造变形研究中的差异与相似点，通过定性和定量（如坡角、断层倾角等）的方法，分析了两种方法的异同点。DEM与AM模拟结果较为一致，基本反映了AM中石英砂的变形行为。AM中材料选取有限（如硅胶、粘土、微玻璃珠等），而DEM材料选取范围大，但其模拟结果依赖参数选取。AM和DEM作为两种独立的方法，有很好的互补性 [(李长圣,2019;](#李长圣2019) [Li et al.,2021)](#refer-li2021)。

<div id="refer-li2021"></div>
[**LI C.S.**, YIN H.W.*, et al. (2021) Calibration of the discrete element method and modelling of shortening experiments. Front. Earth Sci. 9:636512.](https://doi.org/10.3389/feart.2021.636512)

#### 评审意见 <font color=red>**Excellent**</font> <font color=red>**Important**</font> <font color=red>**Nice**</font> 

- **Jonny Wu(Guest Associate Editor):** The manuscript is an <font color=red>**excellent work**</font> and  <font color=red>**important to publish**</font>.  
- **Stuart Hardy:** This is an <font color=red>**important paper**</font> from a methodological point of view - <font color=red>**a reference almost**</font>.
- **Amanda Hughes:** This study does a <font color=red>**nice job**</font> filling an existing need in modeling based studies.


#### 题目

Calibration of the discrete element method and modelling of shortening experiments

#### 作者
Changsheng Li <sup>1,2,3,4</sup>, Hongwei Yin<sup>3*</sup>, Chuang Wu<sup>3</sup>, Yingchun Zhang<sup>3</sup>, Jiaxing Zhang<sup>3</sup>,
Zhenyun Wu<sup>1,2</sup>, Wei Wang<sup>3</sup>, Dong Jia <sup>3</sup>, Shuwei Guan<sup>4</sup> and Rong Ren<sup>4</sup> 

1. State Key Laboratory of Nuclear Resources and Environment, East China University of Technology, Nanchang, China
2. School of Earth Sciences, East China University of Technology, Nanchang, China
3. School of Earth Sciences and Engineering, Nanjing University, Nanjing, China
4. Research Institute of Petroleum Exploration and Development, PetroChina, Beijing, China

#### 摘要
The discrete element method (DEM) is becoming widely accepted as an effective method for addressing tectonic problems in granular materials. It is capable of reproducing structures observed in the analog model (AM). However, the previous experiments also pointed to variability among DEM models and AMs in the number of fault zones, their dip angle and spacing, and the evolution of the surface slope of a thrust wedge. The accuracy of the DEM depends on the input parameter values, so the calibration of the discrete element method is very important. Microscopic properties of particles and macroscopic properties of loose quartz sand were calibrated through a series of repose angle and biaxial tests. Furthermore, an AM was constructed to simulate the evolution of the thrust wedge to compare with DEM results. DEM and AM results indicate an encouraging overall agreement in model evolution. Based on a new automated wedge quantification method, DEM results were systematically compared with AM results on the number of fault zones, their dip angle and spacing, the evolution of the surface slope of a thrust wedge, and other parameters. **Our study provides a necessary comparison between commonly applied modeling approaches, which is important for more confidently applying these methods to understand real fold and thrust belt systems.**

#### 休止角试验

{{< figure src="Fig.1.jpg" title="" width="300px" >}}
<center>a）室内试验三维视图 b）室内试验正视图 c）当 μ=0.3时，离散元模拟结果。</center>
<center>**休止角试验**</center>


{{< figure src="Fig.2.jpg" title="" width="400px" >}}
<center>**颗粒集合体的休止角 θ与颗粒间摩擦系数 μ的关系**</center>

#### 双轴剪切试验

{{< figure src="Fig.3.jpg" title="" width="300px" >}}
<center>a）随机生成颗粒，颗粒直径较小，为 0.1 0.2 0.25和 0.3 mm b）半径膨胀颗粒之间变为 0.2 0.4 0.5和 0.6 mm；；c) 删除虚线外颗粒；d）设置颜色 ；e)颗粒的应变 20%时的形变；f)试样的变形应变场，颜色深浅表征剪切应变的大小，红色 表示 顺时针剪切，蓝色 表示 逆时针剪切，计算方法见 [Morgan(2015)](#Morgan2015)。</center>
<center>**双轴试验过程**</center>

{{< figure src="Fig.4.jpg" title="" width="600px" >}}
<center>a）不同围压下，试样的应力应变曲线 b）双轴试样的莫尔强度包络线。</center>
<center>**当颗粒间摩擦系数 μ=0.3时，双轴试验。**</center>

{{< figure src="Fig.6.jpg" title="" width="500px" >}}
<center>其中，圆点是 [Klinkmüller et al.(2016)](#Klinkmüller2021)给出的环剪试验的结果 ，五角星为本文DEM计算结果。</center>
<center>**室内试验测得的内摩擦角与粘聚力与DEM计算结果对比**</center>

#### 演化过程

{{< figure src="dem_and_am02.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am04.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am08.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am12.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am16.jpg" title="" width="600px" >}}
<center>**第一幅(AM)构造物理模拟；第二幅(DEM)离散元数值模拟；第三幅DEM变形应变图。**</center>

#### 定量对比
{{< figure src="Fig.12.jpg" title="" width="600px" >}}
<center>a）楔体坡角、宽度和高度测量方法示意图；b）物理模拟坡角；c) 楔体宽度演化；d) 楔体高度演化。</center>
<center>**AM和DEM的楔体坡角、宽度和高度演化过程对比图**</center>

#### ZDEM script: 

*表 1  颗粒微观参数表.*

| _d_(mm) &nbsp; | _k_(N·m<sup>−1</sup>) &nbsp; | _ρ_(kg·m<sup>−2</sup>) &nbsp; | _g_(m·s<sup>−2</sup>) &nbsp;&nbsp; |  _f_&nbsp;&nbsp; |  _μ_&nbsp; | _η_(N·s·m<sup>−1</sup>) &nbsp;| _υ_(m·s<sup>−1</sup>) &nbsp;|
| ---------- | ---------------------- | ----------------------- | --------------------- | ------- | ------- | ------------------------ | --------------------- |
|   0.6    |   7.5e3   |   1.3e3    |   10.0   |  0.4&nbsp;&nbsp;  |  0.3&nbsp;&nbsp;  |      0.04&nbsp;&nbsp;   |    &nbsp;0.04&nbsp;  |

>**Note:** The particle packing consists of four particle sizes, with diameters and quantity ratio of 0.2 mm, 0.4 mm, 0.5 mm, and 0.6 mm and 2:2:1:1, respectively. _d_, largest particle diameter. _ρ_, particle density. _g_, gravitational acceleration. _f_, safety factor of the time step. _k_, stiffness of the contact. _μ_, friction coefficient. _η_, dynamic viscosity. _υ_, velocity of the mobile wall.

1. 沉积过程。[gen.py](gen.py) 中内容如下：

    {{< include-code "gen.py" bash >}}

2. 挤压过程。[push.py](push.py) 中内容如下：

    {{< include-code "push.py" bash >}}

#### The quantitative method of the thrust wedge based on mesh (Data) 

{{% notice info %}}
Download：[analog model.7z](analog model.7z) 
{{% /notice %}}

The images of the analog model.


#### 参考文献

<div id="Hardy2009"></div>
[Hardy S, et al (2009) Deformation and fault activity in space and time in high-resolution numerical models of doubly vergent thrust wedges. **Marine and Petroleum Geology** 26:232-248.](https://doi.org/10.1016/j.marpetgeo.2007.12.003)  
<div id="Klinkmüller2021"></div>
[Klinkmüller, M., Schreurs, G., Rosenau, M., and Kemnitz, H. (2016). Properties of Granular Analogue Model Materials: A Community Wide Survey. Tectonophysics 684, 23–38. doi:10.1016/j.tecto.2016.01.017](https://doi.org/10.1016/j.tecto.2016.01.017) 
<div id="Morgan2015"></div>
[Morgan JK (2015) Effects of cohesion on the structural and mechanical evolution of fold and thrust belts and contractional wedges: Discrete element simulations. **Journal of Geophysical Research: Solid Earth** 120:3870-3896.](http://onlinelibrary.wiley.com/doi/10.1002/2014JB011455/full)  
<div id="李长圣2019"></div>
[李长圣 (2019) 基于离散元的褶皱冲断带构造变形定量分析与模拟. **博士论文**. 南京大学.](http://t.cn/Ai9ruJY5) **推荐下载** [最新修订版](https://pan.baidu.com/s/1JWORiC034DwWscT9SiLrGQ) 提取码 `zdem` 
