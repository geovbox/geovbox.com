---
title: Quantitative Analysis and Simulation of Compressional Tectonics Based on Discrete Element Method (Tectonics and Mineralization)
date: 2022-09-01
categories:
    - Paper
tags:
    - Compressional Tectonics
    - Stress and Strain
    - Quantitative Analysis
authors:
    - LI ChangSheng
images:
    - fig4.jpg
slug: 20220901
---


**Download：**

- [Li Changsheng, Yin Hongwei, Xu Wenqiao, Wu Zhenyun, Guan Shuwei, Jia Dong, Ren Rong. Quantitative analysis and simulation of compaction structures based on discrete element method [J]. Geotectonica et Metallogenia, 2022, 46(04): 645-661.](https://doi.org/10.16539/j.ddgzyckx.2022.04.001) 
- The corresponding ZDEM script is provided later in the text.

**The discrete element method (DEM) holds immense potential in the quantitative study of tectonic deformation, stress-strain relationships, and fracture prediction, making it one of the primary directions for future research in quantitative tectonic deformation studies.**

#### Title

Quantitative Analysis and Simulation of Compressional Tectonics Based on Discrete Element Method

#### Authors

Changsheng Li<sup>1,2,3,4</sup>, Hongwei Yin<sup>3\*</sup>, Wenqiao Xu<sup>3</sup>, Zhenyun Wu<sup>1, 2</sup>, 
Shuwei Guan<sup>4</sup>, Dong Jia<sup>3</sup>, Rong Ren<sup>4</sup>

1. State Key Laboratory of Nuclear Resources and Environment, East China University of Technology, Nanchang, China 
2. School of Earth Sciences, East China University of Technology, Nanchang, China 
3. School of Earth Sciences and Engineering, Nanjing University, Nanjing, China
4. PetroChina Research Institute of Petroleum Exploration and Development, Beijing, China



#### Abstract

With advancements in discrete element theory and computer technology, DEM has been widely applied to tectonic simulations across various scales. Compared to traditional sandbox experiments, DEM allows for more precise control of experimental boundary conditions and quantitative analysis of the tectonic deformation process. This facilitates a deeper understanding of the influence of stratigraphic mechanical properties on tectonic deformation at the mesoscopic scale. This paper systematically elaborates on the quantitative analysis method for tectonic deformation based on DEM. Through a typical numerical simulation experiment of compressional tectonics using DEM, we modeled the formation process of tectonic structures under horizontal compression. The study analyzed the changes in stress and strain distribution, as well as the patterns of fracture generation during deformation, yielding the following insights:(1) The simulated tectonics are dominated by foreland-style imbricate thrust faults, with fault activity propagating sequentially from the compression end to regions farther away;(2) Fractures are closely related to fault formation, with the accumulation of numerous fractures in local areas acting as a trigger for fault development;(3) In the early stages of fault formation, material displacement within the fault is minimal, and the incremental increase in fractures is at its peak; in the later stages of fault activity, the incremental increase in fractures decreases;(4) Volumetric strain can characterize fracture types (tensile or compressive), while deformation strain can distinguish between forward and reverse thrust faults;(5) The magnitude of average stress is positively correlated with topographic relief, and the maximum shear stress continuously accumulates at the site of an impending new fault until the fault forms, after which the maximum shear stress dissipates, propagates forward, and accumulates at the next site of an impending fault. These findings demonstrate the significant potential of DEM in the quantitative study of tectonic deformation, stress-strain relationships, and fracture prediction.

<h5> </h5>
{{< figure src="fig2.jpg" title="" width="600px" >}}
<center>(a) Principal Stress Difference and Axial Strain;(b) Shear Strength Envelope</center>
<center><h5>Figure 2: Biaxial Experiment Results</h5></center>

{{< figure src="fig3.jpg" title="" width="600px" >}}
<center><h5>Figure 3: Initial Model</h5></center>

{{< figure src="fig4.jpg" title="" width="600px" >}}
<center><h5>Figure 4: Structural Interpretation of the Wedge at Model Contraction of 1 km (a), 4 km (b), 9 km (c), 16 km (d), and 20 km (e)</h5></center>

{{< figure src="fig6.jpg" title="" width="600px" >}}
<center><h5>Figure 6: Bonded Force Chain Distribution at Contraction of 1 km (a), 4 km (b), 9 km (c), 16 km (d), and 20 km (e) (Blue represents bonded force chains, yellow represents unbonded contacts)</h5></center>

{{< figure src="fig8.jpg" title="" width="400px" >}}
<center><h5>Figure 8: Fault Slip Curves as a Function of Contraction (Faults F1, F2, F3, and F4 as shown in Figure 4; fault slip values measured from the green layer)</h5></center>

{{< figure src="fig9.jpg" title="" width="600px" >}}
<center>In Figure (a), four points are selected from four particles within faults F1, F2, F3, and F4 in the green marker layer. For clarity, the radii of these four particles are magnified threefold. The blue force chains represent bonded force chains within a 1 km radius around the monitoring points.</center>
<center><h5>Figure 9: Motion Paths of Points PF1, PF2, PF3, and PF4 (a); Cumulative Displacement of Points PF1, PF2, PF3, and PF4 with Model Contraction (b); Number of Newly Broken Bonded Force Chains within a 1 km Radius Around Points PF1, PF2, PF3, and PF4 per 1 km of Model Contraction\(c) 
</h5></center>

{{< figure src="fig10.jpg" title="" width="600px" >}}
<center>Here, blue indicates volumetric compression, red indicates volumetric expansion, and the intensity of the color represents the magnitude of volumetric change. In (e), the semi-transparent black layer is the marker layer.</center>
<center><h5>
Figure 10: Cumulative Volumetric Strain in the Model at Contraction of 1 km (a), 4 km (b), 9 km (c), 16 km (d), and 20 km (e)
</h5></center>

{{< figure src="fig15.jpg" title="" width="600px" >}}
<center>Black lines represent stress contours, and black dots indicate points with |deformation strain| > 4, marking fault locations. In Figure (e), the green layer is the marker layer.</center>
<center><h5>
Figure 15: Maximum Shear Stress Distribution at Contraction of 1 km (a), 4 km (b), 9 km (c), 16 km (d), and 20 km (e)
</h5></center>

#### Acknowledgments
The numerical computations in this study were performed on the computing cluster at Nanjing University’s High-Performance Computing Center. The numerical simulation experiments were conducted using discrete element simulation software independently developed by our research group. For more examples of tectonic simulations, see https://geovbox.com. The strain calculation code used in this paper was adapted from scripts by Julia K. Morgan and Thomas Fournier of Rice University, to whom we express our gratitude. The source code for the wedge element measurement program is available at https://github.com/demsheng/Quantitative-wedge. Associate Professors Yu Yixin and Liu Zhina from China University of Petroleum (Beijing) provided thorough and professional reviews of this paper, offering constructive suggestions for improvement, for which we extend our special thanks.

#### ZDEM Script Code

1. Sedimentation Process.[gen.py](gen.py) The content of  is as follows:

    {{< includecode "gen.py" bash >}}

2. Compression Process.[push.py](push.py) The content of  is as follows:

> During the sedimentation process, particles are randomly generated, which may result in differences between the initial model and that described in the paper. Download the initial model from the paper:[init5km_xyr.dat](init5km_xyr.dat) 

    {{< includecode "push.py" bash >}}

---
Translator: Bao Xianjun

