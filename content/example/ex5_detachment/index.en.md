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
Download：
[lsf.sh](/example/ex5_detachment/lsf.sh)
[detachment.py](/example/ex5_detachment/detachment.py)
[pre_struct.gif](/example/ex5_detachment/detachment.gif)
{{% /notice %}}


这里是一个 `滑脱层` 设置的实例，一般地，将滑脱层设置为没有粘结，类似松散石英砂，摩擦系数则可以设置为 0.0。

 `ex5` 目录中文件有
- [lsf.sh](/example/ex5_detachment/lsf.sh)
- [detachment.py](/example/ex5_detachment/detachment.py)
- [init_xyr.dat](/example/ex5_detachment/init_xyr.dat)

## 在终端或 `xshell` 中运行 

```
`bsub < lsf.sh` # 提交计算
`bjobs ` # 查看计算是否提交成功
```

 [lsf.sh](/example/ex5_detachment/lsf.sh) 中内容如下：

{{< include-code "lsf.sh" bash >}}

 [detachment.py](/example/ex5_detachment/detachment.py) 中内容如下：

{{< include-code "detachment.py" bash >}}

得到的演化过程如下：

<h5></h5>
{{< figure src="/example/ex5_detachment/detachment.gif" title="" width="600px" >}}

{{< figure src="/example/ex5_detachment/00.jpg" title="" width="600px" >}}
{{< figure src="/example/ex5_detachment/05.jpg" title="" width="600px" >}}
{{< figure src="/example/ex5_detachment/10.jpg" title="" width="600px" >}}

<center><h5>单位 (km)<br><br>构造演化过程</h5></center>