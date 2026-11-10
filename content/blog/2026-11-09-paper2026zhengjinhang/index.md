---
title: "先存断层倾角如何控制盆地反转？东海西湖凹陷的地震与数值模拟证据（Tectonics）"
date: 2026-11-09
categories:
    - 文章
tags:
    - 东海陆架盆地
    - 西湖凹陷
    - 盆地反转
    - 先存断层
    - 短缩分配
    - 离散元数值模拟
authors:
    - 郑津杭
images:
    - Figure 16.png
slug: "20261109-tectonics-inherited-fault-dip"
description: "结合西湖凹陷嘉兴—宁波地震解释与五组伸展—反转离散元实验，揭示先存断层倾角如何控制原断层逆向再活动、褶皱放大与新生逆冲断层之间的短缩分配，并建立天然构造与数值模型的定量对应。"
---


> **下载原文：** [Zheng et al. (2026), Tectonics, 45, e2025TC009335](https://doi.org/10.1029/2025TC009335)。  
> **软件工具：** 二维离散元软件（ZDEM）。本文的数据可用性声明未列出公开的实验脚本仓库；软件资料及数据说明见文末。

盆地由伸展转入挤压后，原有正断层并不总是沿旧断面高效逆向滑动：有的断层承担了主要短缩，有的只发生部分逆向再活动，还有一些将更多变形转移至盖层褶皱和新生逆冲断层。东海西湖凹陷中央背斜构造带的嘉兴段与宁波段，正展示了这种差异：嘉兴段先存断层较陡，反转背斜更紧闭、构造起伏更高，伴生逆断层更突出；宁波段先存断层倾角较缓，形成较宽缓的背斜，沿原断层的逆向再活动也更连续。针对这一现象，将三维地震资料解释、局部深度域构造测量与五组二维离散元伸展—反转实验结合，追踪断层位移、应变局部化及应力重分布，建立了三类倾角相关的反转响应。**研究的关键贡献，是将“先存断层倾角影响再活动”的几何认识，推进为“先存断层倾角控制短缩如何分配”的过程解释，并用嘉兴—宁波的断层倾角与褶皱几何定量对比加以检验。** 这为解释反转盆地中相邻构造段的差异变形，以及识别原断层再活动、褶皱型构造和新生逆冲构造之间的关系，提供了力学依据。

<div id="refer-Zheng2026"></div>

**论文引用：** Zheng, J., Wu, Z., Tang, X., He, X., Liu, Y., Yan, J., & Miocic, J. M. (2026). Inherited fault angle control on basin inversion structures in the East China Sea: Insights from numerical simulations. *Tectonics, 45*, e2025TC009335. https://doi.org/10.1029/2025TC009335

#### 题目

**Inherited Fault Angle Control on Basin Inversion Structures in the East China Sea: Insights From Numerical Simulations**

**继承性断层角度对东海盆地反转构造的控制作用：来自数值模拟的启示**

#### 作者

Jinhang Zheng<sup>1,2</sup>, Zhiping Wu<sup>1,2</sup>, Xianjun Tang<sup>3</sup>, Xinjian He<sup>3</sup>, Yiming Liu<sup>1,2</sup>, Jinliang Yan<sup>1,2</sup>, and Johannes M. Miocic<sup>4</sup>

1. State Key Laboratory of Deep Oil and Gas, China University of Petroleum (East China), Qingdao, China.
2. School of Geosciences, China University of Petroleum (East China), Qingdao, China.
3. Shanghai Branch of CNOOC Ltd, Shanghai, China.
4. Energy and Sustainability Research Institute, University of Groningen, Groningen, The Netherlands.

#### 摘要

**中文概述**

盆地反转涉及先存伸展构造的收缩再活动，先存断层倾角是影响其再活动潜力的重要因素。研究以西湖凹陷中央背斜构造带嘉兴段与宁波段的差异反转构造为对象，结合地震—地层解释与二维离散元模拟，检验断层倾角如何影响反转过程中的变形分配。实验设置一组不预置先存断层的参考模型，以及初始倾角分别为30°、45°、60°和80°的四组先存断层模型，均经历8 km伸展和随后8 km短缩。结果显示：30°和45°模型以原断层高效逆向再活动为主；60°模型形成部分再活动、褶皱放大与新生逆断层共同作用的混合断层—褶皱体系；80°模型的原断层再活动效率较低，更多短缩由褶皱生长和下盘捷径逆冲断层承担。天然实例中，嘉兴段较陡的先存断层与较紧闭、高起伏的背斜相伴，宁波段较缓的先存断层则与较宽缓、低起伏的背斜和较连续的原断层再活动相伴。地震观测与模型共同支持：倾角相关的短缩分配，是解释嘉兴—宁波背斜构造带差异反转样式的重要机制。

**Abstract（原文）**

Basin inversion involves the contractional reactivation of inherited extensional structures, and inherited fault dip is known to influence reactivation potential: during inversion, lower-angle inherited faults are generally more favorably oriented for reverse reactivation than steep normal faults. In the Xihu Sag of the East China Sea, the Jiaxing and Ningbo segments of the Central Anticline Structural Zone show contrasting inversion styles. The principal inherited faults beneath these segments differ in dip, we combine seismic-stratigraphic interpretation with two-dimensional discrete-element models to test whether inherited fault dip explains this difference. The experiments include one reference model and inherited faults dipping 30°, 45°, 60°, and 80°, each subjected to extension followed by equal-magnitude shortening. The models reproduce three inversion modes: the 30° and 45° faults undergo efficient reverse reactivation and accommodate most shortening by slip reversal along the inherited plane; the 60° fault produces a hybrid fault-fold system in which shortening is partitioned among partial reactivation, fold amplification, and breakthrough thrusting; and the 80° fault is only weakly reactivated as shortening is transferred into fold growth and a footwall shortcut thrust. The Jiaxing segment contains steeper inherited faults associated with tighter and higher-relief folds, whereas the Ningbo segment contains more moderately dipping faults associated with broader, lower-amplitude folds and more continuous inherited-fault reactivation. Together with the seismic observations, these results suggest that dip-dependent shortening partitioning explains the contrasting inversion styles of the Jiaxing and Ningbo segments and provides a framework for interpreting structural differences in inverted rift basins.

### 研究主要内容

#### 1. 从断层“是否再活动”，推进到短缩“由谁承担”

研究同时分析原断层逆向滑动、盖层褶皱放大和新生逆冲断层发育，将断层再活动与整个断层—褶皱体系的变形联系起来。不同倾角对应的关键差异，是这三种变形途径之间的分配关系：倾角较低时，短缩较易沿原弱面集中；倾角增大、原断层逆向滑动受抑制时，变形向邻近褶皱和新生逆断层转移。由此，断层几何被联系到完整的断层—褶皱响应，而不仅是一个最终断面形态。

#### 2. 用位移演化历史区分部分反转与累计净位移反转

断层位移曲线以累计正断位移为正、累计逆断位移为负。短缩阶段曲线下降，表明早期正断位移正在被逆向滑动抵消；只有曲线越过零点，才表示整个伸展—短缩历程的累计净位移转为逆断性质。**因此，“断层正在逆向滑动”“原有正断位移已被全部抵消”和“上方出现反转背斜”不是同一判据。** 30°和45°模型的先存断层出现累计位移过零，而60°和80°模型仍可在未完全抵消早期正断位移的情况下，形成清楚的反转褶皱和新生逆断层。这一过程判别直接服务于地震解释。

#### 3. 将地震解释与模型比较落实到可量化的褶皱几何

研究不仅比较模型与天然剖面“是否相似”，还报告了局部深度转换后的先存断层倾角、T16层位的参照相对起伏和半起伏全宽。嘉兴段断层倾角约65.8°，起伏—宽度比为0.375；宁波段倾角约48.2°，该比值为0.126。模型中60°和45°实验对应指标分别约为0.283和0.084，呈现相同的相对差异。**天然构造、位移历史与褶皱几何三方面相互对应，是本文比单纯终态形态类比更有力的证据。**

#### 4. 将构造继承性的影响贯穿伸展—反转全过程

五组模型先形成伸展断层体系、半地堑及同构造充填，再在同一体系上施加短缩，因而保留了裂陷阶段构造对后续反转的影响。实验比较揭示的是“初始断层倾角—伸展形成的盆地几何—反转短缩分配”的连续关系，而非仅对完全相同的盆地形态改变一个压缩阶段参数。其结果建立了从低倾角再活动主导，到中等倾角混合变形，再到陡倾断层附近褶皱—新生逆冲主导的比较框架。

### 代表性图件与主要研究结果

#### 一、问题的提出：同一反转带为何发育不同形态的背斜？

西湖凹陷经历早期伸展及后续收缩再活动。中央背斜构造带内，嘉兴和宁波两个相邻区段的代表性剖面，在局部半地堑宽度、断层间距及断层密度总体可比的条件下，显示不同的主断层倾角与反转样式：前者较紧闭、起伏较高并伴生更明显的逆断层，后者较宽缓且沿原断层的再活动更连续。这一差异构成模型比较的天然出发点，而非先给定一种统一的反转模式再寻找对应实例。

{{< figure src="Figure2.jpg" title="" width="900px" >}}
<h5>Figure 2. 东亚板块背景、东海盆地构造格架及西湖凹陷T16地震界面时间构造图。研究区图展示主要断层、构造分区、井位、三维地震调查范围及嘉兴AA′和宁波BB′剖面位置，为沿同一反转带开展对比提供空间背景。色彩代表T16界面的双程走时，而非地形高程。</h5>

*Figure 2. (a, b) Plate-tectonic setting of East Asia. (c) Structural framework of the East China Sea Basin. (d) Two-way-traveltime (TWT) structure map of the interpreted T16 seismic horizon in the Xihu Sag, showing faults, structural zones, wells, seismic profiles AA′ and BB′, and the 3D seismic survey extent.*

{{< figure src="Figure7.jpg" title="" width="800px" >}}
<h5>Figure 7. 嘉兴段AA′和宁波段BB′代表性地震剖面及解释。粗黑线突出用于对比的主要先存正断层，图内箭头指示有依据约束的反转期滑动方向。天然剖面揭示先存伸展构造、反转褶皱与伴生逆断层的组合关系。用于精确倾角及褶皱几何比较的是其中局部深度转换窗口，见Figure 16，不能将整条区域时间剖面视作等比例深度剖面。</h5>

*Figure 7. Representative interpreted seismic sections extracted from the 3D seismic volume. (a) Section AA′ across the Jiaxing segment of the Central Anticline Structural Zone. (b) Section BB′ across the Ningbo segment. Locations are shown in Figure 2d. Thicker black lines highlight the principal inherited faults used in the comparison; horizon labels and slip indicators follow the original interpretation.*

#### 二、实验设计：同一加载序列下比较不同先存断层倾角

研究采用VBOX二维离散元方法，设置初始宽40 km、厚10 km的可变形颗粒体系，每组约15万个颗粒。基底由两块刚性板组成：一块固定，另一块与右侧边界共同移动，在板块接触处形成基底速度不连续界面（VD）。五组实验分别为无预置先存断层的参考模型，以及初始倾角30°、45°、60°和80°的弱带模型。

各模型先伸展8 km，宽度由40 km增至48 km，伸展率为20%；随后短缩8 km，按反转初始48 km宽度计算，短缩率为16.7%。在伸展4 km和8 km阶段加入同构造标志层，记录盆地充填及其后续变形。相同的位移历程和材料设置，使不同模型的反转响应能够进行对照。这里的基底VD是施加的速度对比边界，并不是自由滑动的天然拆离层。

{{< figure src="Figure6.jpg" title="" width="900px" >}}
<h5>Figure 6. 五组离散元模型的初始构型。（a）不预置先存断层的参考模型；（b–e）先存弱带倾角分别为80°、60°、45°和30°的模型。（f）引自Li（2019）的不同颗粒摩擦系数下差应力—轴向应变参考曲线，用于说明接触摩擦与颗粒集合体整体力学响应的关系，不是本文新增的一组倾角实验结果。</h5>

*Figure 6. Initial configurations of the DEM models. (a) Reference model without an inherited fault. (b–e) Models with inherited weak zones dipping at 80°, 60°, 45°, and 30°, respectively. VD denotes the basal velocity discontinuity. (f) Reference differential stress–axial strain curves for different interparticle friction coefficients, adapted from Li (2019).*

#### 三、过程证据：中等倾角模型如何产生断层—褶皱耦合？

60°实验展示了最具代表性的过渡响应。伸展阶段，先存断层F1及另一条边界断层F2共同限定盆地，随后出现次级断层与Y形组合。短缩开始后，两条主断层累计正断位移减小，但至8 km短缩时仍未完全过零；与此同时，断层间褶皱放大，并形成连接原断层体系的新生反向逆冲断层F6。应变集中及最大剪应力的重新分布，显示变形并非始终沿原弱面集中，而是在主断层交汇部位、褶皱及新断层之间重新分配。

{{< figure src="Figure10.jpg" title="" width="1000px" >}}
<h5>Figure 10. 60°先存断层模型的伸展—反转演化。三列依次表示叠加于颗粒地层上的畸变应变、二维体积应变及最大剪应力；四行分别对应4 km、8 km伸展及4 km、8 km短缩。F1为预置先存断层，其余标注断层在实验中形成。二维体积应变表征颗粒集合体的局部扩容或压密，不表示单个颗粒的体积变化。</h5>

*Figure 10. Distortional strain superimposed on the colored strata (column 1), two-dimensional volumetric strain (column 2), and maximum shear stress (column 3) for the 60° inherited-fault model at (a) 4 km and (b) 8 km of extension, followed by (c) 4 km and (d) 8 km of shortening. F1 is the inherited fault; F2–F6 formed during the experiment.*

#### 四、数值模型位移演化历史：发生逆向再活动，不等于累计位移已经完全反转

Figure 14将四组先存断层F1的位移历史放在一起，直接显示反转阶段的差异。30°和45°模型中，继承性断层F1能够高效容纳逆向滑动，累计位移曲线穿过零点；60°和80°模型中，继承性断层F1累计正位移虽然下降，但仍保留伸展形成的净位移分量，更多短缩通过褶皱和新生逆断层消纳。

{{< figure src="Figure14.jpg" title="" width="850px" >}}
<h5>Figure 14. 不同初始倾角先存断层在伸展及反转阶段的位移演化。正值与负值分别表示累计净正断位移和累计净逆断位移。短缩阶段曲线下降记录逆向再活动对早期正断位移的抵消，穿过零点才表示累计净位移由正断性质转为逆断性质。</h5>

*Figure 14. Displacement behavior of inherited faults during extension and inversion for different initial dip angles. Positive and negative displacement values denote net cumulative normal-sense and reverse-sense displacement, respectively.*

#### 五、机制归纳：三类反转模式总结，而非一种统一的断层逆冲模式

| 模型中的初始先存断层倾角 | 主要变形途径 | 代表性反转表现 |
| --- | --- | --- |
| 30°—45° | 原断层高效逆向再活动 | 较多短缩集中为沿旧断面的逆向滑动，褶皱相对较宽缓；先存F1累计净位移可过零 |
| 60° | 部分再活动、褶皱放大及新生逆断层共同作用 | 形成混合断层—褶皱体系，新生反向逆冲断层参与变形分配 |
| 80° | 褶皱生长与新生逆冲断层承担更多短缩 | 陡倾原断层逆向再活动效率较低，形成下盘捷径逆冲断层并转移变形 |

倾角的作用体现为应力在断层面上的分解与滑动阻力差异，以及由此产生的变形重新分配。随着先存断层变陡，原弱面不再始终是最有效的短缩吸收途径，体系可通过褶皱放大和新断层形成继续变形。本文的角度组别用于定义给定模型条件下的比较响应，不是自然界普遍适用的单一临界角度；褶皱最终几何同时保留了前期伸展盆地形态的影响。

{{< figure src="Figure15.jpg" title="" width="900px" >}}
<h5>Figure 15. 不同倾角模型的最终伸展构型、最终短缩构型及三类反转机制综合图。（a–d）30°、45°、60°和80°模型的伸展终态；（e–h）对应的短缩终态；（i–k）依次概括高倾角、中等倾角和低倾角反转响应。断面上的σn与τ箭头分别示意局部法向压应力与剪切牵引方向。下部块体图为二维模拟结果的概念归纳，不代表进行了三维数值实验。</h5>

*Figure 15. (a–d) Final extensional-stage geometries for inherited faults dipping at 30°, 45°, 60°, and 80°. (e–h) Corresponding final shortening-stage geometries. (i–k) Schematic synthesis of the high-angle, intermediate, and low-angle inversion regimes. Paired arrows indicate conceptual local directions of normal compression, σn, and shear traction, τ.*

#### 六、实例对比验证与褶皱幅度/宽度比值的定量化：嘉兴与宁波的差异不止于视觉形态

对局部深度转换后的剖面，研究选择主先存断层中较平直、受后期旋转影响较小的基底段测量倾角，并以T16地层界面比较褶皱几何。具体的量化结果如下：

| 天然构造指标 | 嘉兴段 | 宁波段 |
| --- | ---: | ---: |
| 主先存断层剖面倾角 | &emsp;约65.8° | &emsp;约48.2° |
| T16参照相对构造起伏（km） | &emsp;约0.72 | &emsp;约0.52 |
| 半起伏全宽（km） | &emsp;约1.91 | &emsp;约4.13 |
| 起伏／宽度比 | &emsp;0.375 | &emsp;0.126 |
| 对应的比较模型 | &emsp;60°模型 | &emsp;45°模型 |
| 比较模型中的起伏／宽度比 | &emsp;约0.283 | &emsp;约0.084 |

嘉兴段的褶皱起伏较高而特征宽度较小，宁波段的褶皱起伏较低但更宽。60°模型同样表现出比45°模型更集中的褶皱几何，并伴随部分再活动及新生逆断层；45°模型则表现为更高效的原断层累计位移反转和较宽缓的褶皱。**断层倾角、褶皱集中程度和再活动方式的共同对应，使模型—天然对比不再局限于“形似”，而具有一致的几何与运动学依据。**

{{< figure src="quantitative_summary.jpg" title="" width="850px" >}}
<h5>数据摘要图（本介绍稿依据原文数值新绘，非原论文图版）。天然T16界面与选定模型边界的起伏／半起伏全宽比。柱高采用主文第5.2节报告值；实色柱表示天然剖面，斜线柱表示模型。该图补充展示相对褶皱集中程度，不替代原文Figure 16的地震—模型对应。</h5>

{{< figure src="Figure16.jpg" title="" width="1000px" >}}
<h5>Figure 16. 局部深度转换后的天然地震解释与二维DEM结果对比。（a）嘉兴段局部解释；（b）60°模型短缩终态；（c）宁波段局部解释；（d）45°模型短缩终态。嘉兴段较陡的先存断层与紧闭、高起伏反转背斜及新生逆断层相伴，宁波段较缓的先存断层则与宽缓背斜及较连续的原断层再活动相伴。该图是全文天然证据与力学机制的综合对照，建议作为网页封面和核心展示图。</h5>

*Figure 16. Comparison of locally depth-converted seismic interpretations and two-dimensional DEM results. (a) Jiaxing interpretation from the local window in Figure 7a. (b) Final shortening-stage configuration of the 60° model. (c) Ningbo interpretation from the local window in Figure 7b. (d) Final shortening-stage configuration of the 45° model.*

### Conclusions｜主要结论

**（1）先存断层倾角控制反转阶段的缩短应变分配。** 在本文二维DEM模型中，30°和45°先存断层较高效地容纳逆向滑动；60°模型表现为部分再活动、褶皱放大和新生逆断层共同作用；80°模型则将更多缩短应变分配转移至褶皱和下盘逆冲捷径断层。

**（2）位移演化历史能够区分部分逆向再活动与累计净位移反转。** 先存断层累计正断位移减小，说明反向滑动正在抵消早期伸展位移；只有累计位移过零，才表明净位移性质已经转为逆断。

**（3）地震实例解释与模型响应具有一致的几何和运动学差异。** 嘉兴段约65.8°的先存断层与紧闭、高起伏褶皱及较明显的伴生逆断层相伴，宁波段约48.2°的断层则与宽缓褶皱和较连续的原断层再活动相伴；T16构造界面的起伏—宽度比及模型对应指标进一步支持这一对比。

**（4）研究建立了理解差异反转构造的力学框架与机制。** 先存断层倾角通过改变原断层再活动、褶皱放大与新生逆断层之间的缩短分配，影响反转盆地的断层—褶皱组合，为反转盆地构造解释和断层控制圈闭的几何分析提供参考。

#### Acknowledgments｜致谢

本研究使用ZDEM软件开展离散元模拟。作者感谢编辑和审稿人对构造与运动学术语、图件表达、定量描述及模型—天然对比适用范围提出的建议；感谢Rice University的Julia Morgan提供RICEBAL v5.4代码及模型后处理脚本与算法，感谢ChangSheng Li在数值模拟方面的建议，以及中国海油相关研究单位提供地震和井资料。

研究得到国家自然科学基金（**42302155、42572170**）和国家科技重大专项（**2025ZD1402802**）资助。以上基金信息依据本文正式发表版本。

### Data Availability Statement｜数据与软件

本文数据可用性声明给出的ZDEM网站为 [http://geovbox.com/en/](http://geovbox.com/en/)，提供VBOX 2.1的手册、教程、示例和参考资料。论文所用地震反射资料、井资料及构造图由中国海油上海分公司提供，**不能公开发布**。

正式发表版本未列出实验脚本的公开存储地址；VBOX网站提供的是通用软件资料，而非本文完整实验输入与输出的公开下载包。

#### References｜主要参考文献

1. **Zheng, J., Wu, Z., Tang, X., He, X., Liu, Y., Yan, J., & Miocic, J. M. (2026).** Inherited fault angle control on basin inversion structures in the East China Sea: Insights from numerical simulations. *Tectonics, 45*, e2025TC009335. https://doi.org/10.1029/2025TC009335
2. **Sibson, R. H. (1995).** Selective fault reactivation during basin inversion: Potential for fluid redistribution through fault-valve action. *Geological Society, London, Special Publications, 88*(1), 3–19. https://doi.org/10.1144/GSL.SP.1995.088.01.02
3. **Turner, J. P., & Williams, G. A. (2004).** Sedimentary basin inversion and intra-plate shortening. *Earth-Science Reviews, 65*(3–4), 277–304. https://doi.org/10.1016/j.earscirev.2003.10.002
4. **Morgan, J. K. (2015).** Effects of cohesion on the structural and mechanical evolution of fold and thrust belts and contractional wedges: Discrete element simulations. *Journal of Geophysical Research: Solid Earth, 120*(5), 3870–3896. https://doi.org/10.1002/2014JB011455
5. **Li, C., Yin, H., Wu, C., Zhang, Y., Zhang, J., Wu, Z., et al. (2021).** Calibration of the discrete element method and modeling of shortening experiments. *Frontiers in Earth Science, 9*, 636512. https://doi.org/10.3389/feart.2021.636512
6. **Li, C. (2019).** Quantitative analysis and simulation of structural deformation in the fold and thrust belt based on discrete element method. Doctoral dissertation, Nanjing University.
