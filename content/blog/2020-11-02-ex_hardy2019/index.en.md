---
title: Discrete Element Simulation of Extensional, Growth, and Fault-Propagation Folds (Basin Research)
date: 2020-11-02
categories:
    - User Examples
tags:
    - Extensional
    - Growth
    - Fault-Propagation Folds
authors:
    - Li Changsheng
    - Xu Wenqiao
images:
    - all_0000260000_ini.jpg
commands:
    - xv
    - yv
slug: 20201102
---

**The example is referenced from[(Hardy,2019)](#refer-hardy2019)**

**The example is referenced from (Hardy, 2019)**

Extensional fault-propagation folds are an important type of fold in extensional environments, caused by the activation of buried normal faults propagating upward, resulting in the bending of overlying strata [(Qi Peng et al., 2009)](chrome-extension://ebldafnijcbblaaabcehdamipojmicmg/index.html#refer-qi2009). [(Hardy, 2019)](chrome-extension://ebldafnijcbblaaabcehdamipojmicmg/index.html#refer-hardy2019) simulated the evolutionary process of extensional fault-propagation folds via discrete element modeling.

Here, a discrete element numerical simulation [(script source code)](chrome-extension://ebldafnijcbblaaabcehdamipojmicmg/index.html#refer-code-1) reproduces the evolutionary process of extensional, growth, and fault-propagation folds. 


<h5> </h5>
{{< figure src="normal_fault_synsed.gif" title="" width="600px" >}}
<center><h5>Unit (km)<br><br>Tectonic Evolution Process</h5></center>

{{< figure src="all_0000020000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000082000.jpg" title="" width="600px" >}}
{{< figure src="all_0000140000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000200000_ini.jpg" title="" width="600px" >}}
{{< figure src="all_0000260000_ini.jpg" title="" width="600px" >}}


<div id="refer-code-1"></div>

## VBOX Script Source Code [normal_fault_synsed.py](normal_fault_synsed.py)

{{< includecode "normal_fault_synsed.py" "bash" >}}

## References

<div id="refer-qi2009"></div>
[1] [Qi Peng and Zhang Junxia. (2009). Research Status of Extensional Fault-Propagation Folds. Journal of Geosciences in Universities, (03), 351-357.](http://t.cn/A6GL9zes)

<div id="refer-hardy2019"></div>

[2] [Hardy, S. (2019). Discrete element modelling of extensional, growth, fault‐propagation folds. Basin Research, 31(3), 584-599.](https://doi.org/10.1111/bre.12335) 

---
Translator: Zhu Suqin


