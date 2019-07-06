---
title: 古隆起
date: 2019-06-29
categories:
    - 示例
tags:
    - 古隆起
    - lsf
authors:
    - 李长圣
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
[lsf.sh](/example/ex6_palaeohigh/lsf.sh)
[detachment.py](/example/ex6_palaeohigh/palaeohigh.py)
[init_xyr.dat](/example/ex6_palaeohigh/init_xyr.dat)
[palaeohigh.gif](/example/ex6_palaeohigh/palaeohigh.gif)
{{% /notice %}}


这里是一个 `古隆起` 设置的实例，将古隆起的 x,y,spin（角速度）固定。

 `ex6` 目录中文件有
 
- [lsf.sh](/example/ex6_palaeohigh/lsf.sh)
- [palaeohigh.py](/example/ex6_palaeohigh/palaeohigh.py)
- [init_xyr.dat](/example/ex6_palaeohigh/init_xyr.dat)

## 进入 `ex6` 目录，在终端或 `xshell` 中运行 

```
$ bsub < lsf.sh   # 提交计算
$ bjobs           # 查看计算是否提交成功
```

 [lsf.sh](/example/ex6_palaeohigh/lsf.sh) 中内容如下：

{{< include-code "lsf.sh" bash >}}

 [palaeohigh.py](/example/ex6_palaeohigh/palaeohigh.py) 中内容如下：

{{< include-code "palaeohigh.py" bash >}}

得到的演化过程如下：

<h5></h5>
{{< figure src="/example/ex6_palaeohigh/palaeohigh.gif" title="" width="600px" >}}

{{< figure src="/example/ex6_palaeohigh/00.jpg" title="" width="600px" >}}
{{< figure src="/example/ex6_palaeohigh/05.jpg" title="" width="600px" >}}
{{< figure src="/example/ex6_palaeohigh/10.jpg" title="" width="600px" >}}

<center><h5>单位 (km)<br><br>构造演化过程</h5></center>



