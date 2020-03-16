---
title: 三行代码实现病毒传播过程模拟（离散元）
date: 2020-03-16
categories:
    - 课程
authors:
    - 李长圣
images:
slug: 20200317
---

在离散元软件VBOX，加入如下三行代码，实现病毒传播过程模拟。
　
```c
	if ((spheres[index_o].color = 1) || (spheres[index_a].color = 1))
	{
		spheres[index_o].color = 1;
		spheres[index_a].color = 1;
	}
```

- 假设：密闭空间有40个健康的蓝色颗粒，所有颗粒自动运动，接触就感染，永远治不好。
- 边界条件：一个编号为0的颗粒突然感染红色病毒，25%(10个)的颗粒开始活动，并带动其他颗粒活动。
- 模拟结果：
	- 都是从第一个病例向外逐渐扩散，离0号红色颗粒越近，感染越快。
	- 无阻尼自由移动的时候，仅幸存一颗粒。
	- 有阻尼自由移动的时候，左边一半颗粒尚未感染。
{{< figure src="damp0.0.gif" title="阻尼=0.0"  >}}
{{< figure src="damp0.2.gif" title="阻尼=0.2"  >}}

