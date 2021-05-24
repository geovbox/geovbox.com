---
title: Syntectonic sedimentation 
date: 2019-01-19
categories:
    - Example
tags:
    - Sed
authors:
    - LI ChangSheng
images:
    - 051.png
commands:
    - restore
---

{{% notice info %}}
数据下载：[syn_sedimentaion.py](syn_sedimentaion.py)
[0000046000.sav](0000046000.sav)
[syn_sedimentaion.gif](syn_sedimentaion.gif)
{{% /notice %}}


这里是一个 `同构造沉积` 计算实例。

## 运行 `vboxdaily syn_sedimentaion.py` 
[syn_sedimentaion.py.py](syn_sedimentaion.py) 中内容如下：

{{< include-code "syn_sedimentaion.py" bash >}}

<h5></h5>
计算结束得到同构造沉积过程：
{{< figure src="syn_sedimentaion.gif" title="同构造沉积过程" width="600px" >}}

{{< figure src="040.png" title="" width="600px" >}}
{{< figure src="050.png" title="" width="600px" >}}
{{< figure src="051.png" title="" width="600px" >}}
{{< figure src="053.png" title="" width="600px" >}}
{{< figure src="056.png" title="" width="600px" >}}
{{< figure src="100.png" title="" width="600px" >}}
<center><h5>单位 (km)<br><br>同构造沉积示例</h5></center>

## 微观参数表

| 颗粒直径  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _d_ (m)  | 颗粒密度  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _ρ_ (kg∙m<sup>-3</sup>)   | 颗粒摩擦系数  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  | 缩短速率 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  _υ_ (m∙s<sup>-1</sup>)|  时间步 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> s |
|---------------|-----------|--------|----------|-------------|
|    60，80   |   2500   |   0.3   |   2.0   |   0.05 |

