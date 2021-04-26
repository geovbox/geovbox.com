---
title: 剥蚀
date: 2019-01-18
categories:
    - 示例
tags:
    - 剥蚀
authors:
    - 李长圣
images:
    - 051.png
commands:
    - restore
    - del
---

{{% notice info %}}
数据下载：[syn_erosion.py](/example/syn_erosion/syn_erosion.py)
[0000046000.sav](/example/syn_erosion/0000046000.sav)
[syn_erosion.gif](/example/syn_erosion/syn_erosion.gif)
{{% /notice %}}


这里是一个 `同构造剥蚀` 计算实例。

 [syn_erosion.py.py](/example/syn_erosion/syn_erosion.py) 中内容如下：

{{< include-code "syn_erosion.py" bash >}}

得到的演化过程如下：

{{< figure src="/example/syn_erosion/colorbar.png" title="" width="600px" >}}
<h5></h5>
{{< figure src="/example/syn_erosion/syn_erosion.gif" title="演化过程" width="600px" >}}

{{< figure src="/example/syn_erosion/040.png" title="" width="600px" >}}
{{< figure src="/example/syn_erosion/050.png" title="" width="600px" >}}
{{< figure src="/example/syn_erosion/051.png" title="" width="600px" >}}
{{< figure src="/example/syn_erosion/060.png" title="" width="600px" >}}
{{< figure src="/example/syn_erosion/100.png" title="" width="600px" >}}
<center><h5>单位 (km)<br><br>构造形态及平均应力、最大剪切应力</h5></center>

## 微观参数表

| 颗粒直径  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _d_ (m)  | 颗粒密度  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _ρ_ (kg∙m<sup>-3</sup>)   | 颗粒摩擦系数  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  | 缩短速率 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  _υ_ (m∙s<sup>-1</sup>)|  时间步 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> s |
|---------------|-----------|--------|----------|-------------|
|    60，80   |   2500   |   0.3   |   2.0   |   0.05 |

