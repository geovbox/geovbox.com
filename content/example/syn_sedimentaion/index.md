---
title: 沉积
date: 2019-01-19
categories:
    - 示例
tags:
    - 沉积
authors:
    - 李长圣
images:
    - 051.png
commands:
    - restore
---

{{% notice info %}}
数据下载：[syn_sedimentaion.py](/example/syn_sedimentaion/syn_sedimentaion.py)
[0000046000.sav](/example/syn_sedimentaion/0000046000.sav)
[syn_sedimentaion.gif](/example/syn_sedimentaion/syn_sedimentaion.gif)
{{% /notice %}}


这里是一个 `同构造沉积` 计算实例。

[syn_sedimentaion.py.py](/example/syn_sedimentaion/syn_sedimentaion.py) 中内容如下：

{{< include-code "syn_sedimentaion.py" bash >}}

<h5></h5>
计算结束得到同构造沉积过程：
{{< figure src="/example/syn_sedimentaion/syn_sedimentaion.gif" title="同构造沉积过程" width="600px" >}}

{{< figure src="/example/syn_sedimentaion/040.png" title="" width="600px" >}}
{{< figure src="/example/syn_sedimentaion/050.png" title="" width="600px" >}}
{{< figure src="/example/syn_sedimentaion/051.png" title="" width="600px" >}}
{{< figure src="/example/syn_sedimentaion/053.png" title="" width="600px" >}}
{{< figure src="/example/syn_sedimentaion/056.png" title="" width="600px" >}}
{{< figure src="/example/syn_sedimentaion/100.png" title="" width="600px" >}}
<center><h5>单位 (km)<br><br>同构造沉积示例</h5></center>

## 微观参数表

| 颗粒直径  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _d_ (m)  | 颗粒密度  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> _ρ_ (kg∙m<sup>-3</sup>)   | 颗粒摩擦系数  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  | 缩短速率 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br>  _υ_ (m∙s<sup>-1</sup>)|  时间步 &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; <br> s |
|---------------|-----------|--------|----------|-------------|
|    60，80   |   2500   |   0.3   |   2.0   |   0.05 |

