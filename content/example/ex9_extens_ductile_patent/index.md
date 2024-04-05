---
title: 韧性基底 伸展构造(附发明专利ZDEM脚本)
date: 2024-04-05
categories:
    - 示例
tags:
    - 伸展构造
authors:
    - 李长圣
images:
    - all_0000046001.png
commands:
    - BOND
---

{{% notice info %}}
数据下载：
[extens_ductile_patent.py](extens_ductile_patent.py) 
{{% /notice %}}


这里是一个 `韧性基底 伸展构造` 设置的实例，基底由左右两个刚性墙和中间的韧性墙组成。  
**粘结时，设置临时半径缩放系数等于初始叠合率，避免出现跨颗粒粘结情况发生**，详细描述见发明专利： 

[李长圣,尹宏伟,吴珍云,等. 一种基于离散元的裂谷盆地伸展过程模拟方法[P]. 江西省：CN111008472B,2023-11-21.](https://kns.cnki.net/kcms2/article/abstract?v=Skeo7MzZydbnlVpkrvNpcHaAaho85ENh5lMs7Wo_-jAc8-dZK0ruYCsA6mSgArEyp_YTsYMNtXzyxpikL8ui74_4-AZtLg58Nxrba3X6a-kR-IT41BiuSQbUO8eh7WPV&uniplatform=NZKPT&flag=copy)

{{< figure src="three_wall.png" title="" width="400px" >}}

- 初始叠合率 cratio=|AO|/(rA+rO), 即圆心距离(|AO|)与平衡距离(rA+rO)的比值
{{< figure src="cratio.png" title="" width="300px" >}}
- 临时半径缩放系数rext=rtmp/rold
{{< figure src="rext.png" title="" width="300px" >}}

- [extens_ductile_patent.py](extens_ductile_patent.py) 中内容如下：
    {{< include-code "extens_ductile_patent.py" bash >}}

- 演化过程如下：

<h5></h5>

{{< figure src="all_0000015001.png" title="初试模型" width="600px" >}}
{{< figure src="all_0000025000.png" title="伸展" width="600px" >}}
{{< figure src="all_0000030001.png" title="沉积1" width="600px" >}}
{{< figure src="all_0000041000.png" title="伸展" width="600px" >}}
{{< figure src="all_0000046001.png" title="沉积2" width="600px" >}}

<center><h5>单位 (km)<br><br></h5></center>

