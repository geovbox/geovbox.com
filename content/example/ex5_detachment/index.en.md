---
title: Set up Detachment
date: 2019-01-20
categories:
    - Example
tags:
    - Fault
authors:
    - LI ChangSheng
images:
    - 10.jpg
commands:
    - LOAD
    - BOND
    - bsub
    - bjobs
---

{{% notice info %}}
数据下载：
[detachment.py](detachment.py)
[pre_struct.gif](detachment.gif)
{{% /notice %}}


这里是一个 `滑脱层` 设置的实例，一般地，将滑脱层设置为没有粘结，类似松散石英砂，摩擦系数则可以设置为 0.0。

[detachment.py](detachment.py) 和 [init_xyr.dat](init_xyr.dat) 需放在同一目录。

 [detachment.py](detachment.py) 中内容如下：

{{< include-code "detachment.py" bash >}}

得到的演化过程如下：

<h5></h5>
{{< figure src="detachment.gif" title="" width="600px" >}}

{{< figure src="00.jpg" title="" width="600px" >}}
{{< figure src="05.jpg" title="" width="600px" >}}
{{< figure src="10.jpg" title="" width="600px" >}}

<center><h5>单位 (km)<br><br>构造演化过程</h5></center>

## 参考文献

- [李长圣，尹宏伟. 滑脱层强度对挤压构造的影响:离散元数值模拟. **2017中国地球科学联合学术年会论文集**,2017:4. ](http://t.cn/E6k57Mg)