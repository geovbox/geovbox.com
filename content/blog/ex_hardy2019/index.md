---
title: 伸展、生长、断层传播褶皱的离散元模拟(Basin Research)
date: 2020-11-02
categories:
    - 用户实例
tags:
    - 伸展
    - 生长
    - 断层传播褶皱
authors:
    - 李长圣
    - 徐雯峤
images:
    - all_0000260000_ini.jpg
commands:
    - xv
    - yv
slug: 20201102
---

**实例参考自[(Hardy,2019)](#refer-hardy2019)**

伸展断层传播褶皱是伸展环境中重要的一种褶皱类型，是由于隐伏基底正断层活化向上传播而引起上覆地层发生的弯曲[(祁鹏等,2009)](#refer-qi2009)。[(Hardy,2019)](#refer-hardy2019)基于离散元模拟了伸展断层传播褶皱的演化过程。  

这里通过一个离散元数值模拟[(脚本源码)](#refer-code-1)再现了伸展、生长、断层传播褶皱演化过程。  


<h5> </h5>
{{< figure src="normal_fault_synsed.gif" title="" width="600px" >}}
<center><h5>单位 (km)<br><br>构造演化过程</h5></center>

{{< figure src="all_0000020000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000082000.jpg" title="" width="600px" >}}
{{< figure src="all_0000140000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000200000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000260000_ini.jpg" title="" width="600px" >}}


<div id="refer-code-1"></div>

## VBOX脚本源码 [normal_fault_synsed.py](normal_fault_synsed.py)


{{< include-code "normal_fault_synsed.py" bash >}}

## 参考文献

<div id="refer-qi2009"></div>
[1] [祁鹏 和 张俊霞.(2009).伸展断层传播褶皱研究现状. 高校地质学报(03),351-357.](http://t.cn/A6GL9zes)  

<div id="refer-hardy2019"></div>
[2] [Hardy, S. (2019). Discrete element modelling of extensional, growth, fault‐propagation folds. Basin Research, 31(3), 584-599.](https://doi.org/10.1111/bre.12335)  




