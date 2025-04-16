---
title: Normal Distribution Nail Board Experiment
date: 2021-03-23
categories:
    - User Examples
tags:
    - Normal Distribution
authors:
    - Zhong Jun
images:
    - 0.png
commands:
    - gline
slug: 20210323
---

> Script and Data Download:
> Nail Coordinates: [init_xyr.dat](chrome-extension://ebldafnijcbblaaabcehdamipojmicmg/init_xyr.dat)
> VBOX Script: [normal_distribution.py](chrome-extension://ebldafnijcbblaaabcehdamipojmicmg/normal_distribution.py)normal_distribution.py)



This is a normal distribution nail board experiment completed based on discrete element numerical simulation.

In the figure below, each gray dot represents a nail, and the distances between them are equal. The horizontal position of each nail in the upper layer is precisely located between the two nails in the lower layer. A certain number of small balls, with a diameter smaller than the distance between two nails, are generated above the nail area and dropped down at the entrance. The small balls propagate downward in the nail board area until they fall into the bottom board. A large number of identical small balls continuously drop from the entrance, and as long as the number of balls is sufficiently large, they will form an approximate normal density function pattern on the bottom board (i.e., high in the middle, low at both ends, resembling a bell shape).

## <strong>Dynamic Diagram</strong>
{{< figure src="normal_distribution.gif" title="" >}}


## <strong>Static Process</strong>

|       |       |        |        |
| :-----| ----: | :----: | :----: |
| {{< figure src="1.png" title=""  >}}  | {{< figure src="2.png" title=""  >}}  | {{< figure src="3.png" title=""  >}}  | {{< figure src="4.png" title=""  >}}  |
|       |       |        |        |


## VBOX Script Source Code [normal_distribution.py](normal_distribution.py)

{{< includecode "normal_distribution.py" bash >}}

---
Translator: Zhu Suqin