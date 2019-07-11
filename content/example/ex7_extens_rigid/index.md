---
title: 刚性基底 伸展构造
date: 2019-06-29
categories:
    - 示例
tags:
    - 伸展构造
    - lsf
authors:
    - 李长圣
images:
    - 06.jpg
commands:
    - LOAD
    - BOND
    - bsub
    - bjobs
---

{{% notice info %}}
数据下载：
[lsf.sh](/example/ex7_extens_rigid/lsf.sh)
[detachment.py](/example/ex7_extens_rigid/extens_rigid.py)
[init_xyr.dat](/example/ex7_extens_rigid/init_xyr.dat)
[extens_rigid.gif](/example/ex7_extens_rigid/extens_rigid.gif)
{{% /notice %}}


这里是一个 `刚性基底 伸展构造` 设置的实例，使用上下两个刚性板完成。

 `ex5` 目录中文件有
 
- [lsf.sh](/example/ex7_extens_rigid/lsf.sh)
- [extens_rigid.py](/example/ex7_extens_rigid/extens_rigid.py)
- [init_xyr.dat](/example/ex7_extens_rigid/init_xyr.dat)

## 进入 `ex7` 目录，在终端或 `xshell` 中运行 

```
$ bsub < lsf.sh   # 提交计算
$ bjobs           # 查看计算是否提交成功
```

 [lsf.sh](/example/ex7_extens_rigid/lsf.sh) 中内容如下：

{{< include-code "lsf.sh" bash >}}

 [extens_rigid.py](/example/ex7_extens_rigid/extens_rigid.py) 中内容如下：

{{< include-code "extens_rigid.py" bash >}}

得到的演化过程如下：

<h5></h5>
{{< figure src="/example/ex7_extens_rigid/extens_rigid.gif" title="" width="600px" >}}

{{< figure src="/example/ex7_extens_rigid/00.jpg" title="" width="600px" >}}
{{< figure src="/example/ex7_extens_rigid/02.jpg" title="" width="600px" >}}
{{< figure src="/example/ex7_extens_rigid/04.jpg" title="" width="600px" >}}
{{< figure src="/example/ex7_extens_rigid/06.jpg" title="" width="600px" >}}
{{< figure src="/example/ex7_extens_rigid/08.jpg" title="" width="600px" >}}

<center><h5>单位 (km)<br><br>构造演化过程</h5></center>

## 参考文献

-  李长圣，尹宏伟*，张佳星，汪伟. 琼东南盆地基底断层性质对凹陷沉积模式的影响：基于离散元数值模拟的认识. **2018中国地球科学联合学术年会论文集**, 北京, 2018.



