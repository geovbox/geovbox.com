---
title: Quantitative Analysis and Modeling of Structural Deformation in Fold-Thrust Belts Based on the Discrete Element Method
date: 2021-07-21
categories:
    - Dissertation
    - Doctor
authors:
    - Changsheng Li
images:
    - 1.jpg
slug: 20210721
---

#### Title: Quantitative Analysis and Numerical Modeling of Structural Deformation in Fold-Thrust Belts Using the Discrete Element Method
#### Author: Changsheng Li
#### Abstract
The Discrete Element Method (DEM), as a novel approach for studying structural deformation, enables quantitative observation and analysis of stress and strain evolution within models. This method aids in revealing the deformation characteristics and mechanisms of fold-thrust belts, as well as evaluating the influence of stress-strain distribution on the physical properties of hydrocarbon reservoirs, demonstrating significant theoretical and practical value.Building upon literature review, field geological investigations, seismic profile interpretation, and analog tectonic modeling, this study employs DEM-based numerical simulations to comprehensively analyze the structural deformation features, evolutionary mechanisms, and controlling factors of fold-thrust belts. The main findings include:

1. A structured array was employed to construct the fundamental data architecture of the Discrete Element Method (DEM). The grid-based neighbor search algorithm was optimized to accelerate neighbor detection and contact evaluation. By reorganizing the modules for neighbor search, contact judgment, and contact force updates, a lock-free and high-efficiency parallel computing framework was achieved. The linear elastic and Hertz-Mindlin contact mechanics models were integrated to develop VBOX, a highly scalable and high-performance DEM program tailored for tectonic simulations, along with a standardized testing protocol.
2. The concepts of equivalent parameters and equivalent models were introduced. Through angle-of-repose and biaxial tests, the mesoscopic parameters of quartz sand particles reflecting macroscopic mechanical properties were calibrated. A comparative study between physical analog modeling and DEM numerical simulation was designed, proposing a grid-based quantitative analysis method for thrust wedges. Key geometric parameters (e.g., slope angle, fault dip) were systematically compared to evaluate the similarities and differences between these two approaches in studying tectonic deformation.
3. A comprehensive correspondence table between particle-scale mesoscopic parameters and rock macroscopic properties was established via systematic DEM simulations. The controlling effects of stratigraphic cohesion, internal friction angle, décollement strength, and thickness on fold-thrust belt evolution were investigated. Quantitative analysis of deformation characteristics and mechanisms provided foundational support for advancing theories of complex fold-thrust systems. Low-cohesion strata exhibit dispersed strain distribution with random fracture networks, while high-cohesion strata develop localized strain with larger fault displacements and potential back-thrusts. Weakly cohesive rocks with diffuse fractures form porous reservoirs favorable for hydrocarbon storage, whereas strongly cohesive rocks develop fracture corridors serving as preferential migration pathways. Décollement strength predominantly controls structural style: high-friction décollements produce forward-propagating imbricate thrusts, whereas low-friction décollements generate pop-up structures with alternating fore- and back-thrusts. Stratigraphic competence shows minor influence, with overall deformation mainly governed by basal décollement strength. Décollement thickness exhibits negligible impact on structural patterns.
4. Focusing on the Cenozoic Kuqa fold-thrust belt, mesoscopic parameters corresponding to rock salt macro-properties were calibrated. Numerical simulations demonstrated that syn-tectonic sedimentation critically controls deformation partitioning, revealing its key role in the Qiulitag salt diapir evolution. Salt produces vertically stratified deformation: sub-salt structures feature closely spaced thrust faults, while supra-salt domains develop broad folds. Initial salt basin width was identified as the primary factor controlling along-strike structural variability in western Kuqa. Lateral segmentation of deformation results from variations in initial salt basin width and thickness. Stress stratification divides the section into three domains: maximum stress below salt, minimum stress within salt, and intermediate stress above salt. Salt flow exhibits directional preference, with layer-parallel movement enhanced by syn-tectonic sedimentation, showing overall flow direction consistent with compression.

#### Keywords: discrete element method; parallel computing; stress-strain; thrust wedge; salt tectonics
#### Contents：
1. Prolegomenon
    + 1.1 Significance of Research and Rationale for Topic Selection 
    + 1.2 Research Status of Quantitative Analysis Methods for Tectonic Deformation 
        + 1.2.1 Balanced cross - section technique 
        + 1.2.2 Critical Angle Coulomb Wedge Model 
        + 1.2.3 Tectonic physical simulatio 
        + 1.2.4 Tectonic numerical simulation
    + 1.3 Summary of This Paper 
    + 1.4 Methodology and Technical Implementation Framework 
    + 1.5 Innovative Contributions 
2. Development and Validation of Discrete Element Software
    + 2.1 Discrete Element Theory and Software 
    + 2.2 Data Structure 
    + 2.3 Neighbor Searching and Contact Detection 
    + 2.4 Particle Position Update 
    + 2.5 Contact Force Calculation 
        + 2.5.1 Linear Elastic Model
        + 2.5.2 Hertz-Mindlin Contact Model 
    + 2.6 Damping and Time Step 
    + 2.7 Stress-Strain Characterization Methods 
        + 2.7.1 Stress 
        + 2.7.2 Strain 
    + 2.8 Concurrent Design 
    + 2.9 Concurrent Design 
        + 2.9.1 Single Particle 
        + 2.9.2 Two Particles 
        + 2.9.3 Particle Aggregate 
    + 2.10 Summary 
3. Parameter Selection and Calibration in Structural Numerical Simulation 
    + 3.1 Equivalent Parameters and Equivalent Models 
    + 3.2 Calibration of Discrete Element Mesoscopic Parameters for Quartz Sand 
        + 3.2.1 Angle of Repose Test 
        + 3.2.2 Biaxial Test 
        + 3.2.3 Summary 
    + 3.3 Physical Simulation 
    + 3.4 Numerical Simulation 
    + 3.5 Comparison Between Physical and Numerical Simulations 
        + 3.5.1 Deformation and Strain Analysis 
        + 3.5.2 Structural Interpretation 
        + 3.5.3 Wedge Evolution 
    + 3.6 Summary 
4. Deformation Mechanisms and Influencing Factors of Fold-Thrust Belts 
    + 4.1 Parameter Selection and Tuning 
    + 4.2 Initial Conditions and Computational Equipment 
    + 4.3 Rock Layer Cohesion 
    + 4.4 Internal Friction Angle of Rock Layers 
    + 4.5 Rock Layer Thickness 
    + 4.6 Influence of Detachment Layers on Structural Deformation of Fold-Thrust Belts 
        + 4.6.1 Strength of Basal Detachment Layers 
        + 4.6.2 Thickness of Basal Detachment Layers 
        + 4.6.3 Discussion 
    + 4.7 Summary 
5. Numerical Simulation of Salt Structures in Fold-Thrust Belts
    + 5.1 Salt Rocks and Salt Structures 
    + 5.2 Mesoscopic Parameters of Salt Rock Particles 
    + 5.3 Numerical Simulation of the Kuqa Foreland Basin 
        + 5.3.1 Syn-tectonic Sedimentation 
        + 5.3.2 Initial Salt Basin Width 
        + 5.3.3 Salt Layer Thickness 
    + 5.4 Summary 
6. Conclusions and Future Directions 
    + 6.1 Conclusions 
    + 6.2 Future Directions 
7. Appendix 
    + 7.1 Hardware and Software Environment 
    + 7.2 Numerical Simulation of Biaxial Tests on Quartz Sand 
    + 7.3 Biaxial Tests on Rocks 
        + 7.3.1 Biaxial Test Results Under Different Confining Pressures 
        + 7.3.2 Biaxial Test Results Under Different Friction Coefficients 
        + 7.3.3 Biaxial Test Results Under Different Bond Parameters 
    + 7.4 Growth Fault 
    + 7.5 Test Cases N0, N1, S0, and S1 
    + 7.6 Plane Geometry in Discrete Element Method 192
    + 7.7 Initial Conditions and Computational Equipment M1C1, M1C2, M2C1, M3C1, M4C1 
    + 7.8 Rock Layer Cohesion C1, C10, C19, C24 
    + 7.9 Internal Friction Angle of Rock Layers φ5, φ13, φ17, φ20, 217
    + 7.10 Strength of Basal Detachment Layers μ0, μ1, μ2, μ3
    + 7.11 Thickness of Basal Detachment Layers D0, D300, D500, D1000 
* 8 References 

#### Relevant Literature

1. [**Changsheng Li** (2019) Quantitative Analysis and Simulation of Structural Deformation in Fold-Thrust Belts Based on Discrete Element Method. **Doctoral Dissertation**. Nanjing University.](http://t.cn/Ai9ruJY5) **Recommended Download** [Latest Revised Edition](https://pan.baidu.com/s/1JWORiC034DwWscT9SiLrGQ) Extraction Code `zdem`  
- **Changsheng Li**, Yin, H.W.*,et al.**(2021)** Quantitative Analysis and Simulation of Compressional Structures Based on Discrete Element Method. Tectonics and Metallogeny. (Accepted for Publication)
- [**Li, C.S.**, Yin, H.W.*, , et al.**(2021)** Effects of salt thickness on the structural deformation of foreland fold-and-thrust belt in the Kuqa Depression, Tarim Basin: Insights from discrete element models. Frontiers in Earth Science, 9:655173.](https://doi.org/10.3389/feart.2021.655173)
- [**Li, C.S.**, Yin, H.W.*, et al.**(2021)** Calibration of the discrete element method and modelling of shortening experiments. Frontiers in Earth Science, 9:636512.](https://doi.org/10.3389/feart.2021.636512)
- [**LI C.S.**, YIN H.W.*, et al. **(2018)**. Validation Tests for Discrete Element Codes Using Single-Contact Systems. International Journal of Geomechanics 18, 06018011.7.](https://ascelibrary.org/doi/10.1061/(ASCE)GM.1943-5622.0001133)  
- [**LI C.S.**,YIN H.W.*,Chun Liu, Shenyang Cai. **2017** Design and Testing of Shared-Memory Parallel Discrete Element Program. Journal of Nanjing University (Natural Sciences),(06):1161-1170.](http://t.cn/EiaL0Ad)  

#### Invention Patent
1. **LI C.S.**,Rong Ren,Shuwei Guan,Hongwei Yin. A Discrete Element-Based Simulation Method and Device for the Uplift Process of Paleo-Uplifts [P]. Application Date: 2021. (To be Published)
- [**LI C.S.**,YIN H.W.,Zhenyun Wu,Dong Jia,Wenqiao Xu,Wei Wang. A Discrete Element-Based Simulation Method for the Extension Process of Rift Basins[P]. CN111008472A,Application Date：2019-12-02](https://kns8.cnki.net/kcms/detail/detail.aspx?dbcode=SCPD&dbname=SCPD2020&filename=CN111008472A)  

#### Software Copyright：
1. **Post-processing System for Discrete Element Numerical Simulation** V1.0. East China University of Technology, Jun Zhong, **LI C.S.**, Wenqiao Xu,Huajing Wei , Zhenyun Wu. **2021**.  
- **Virtual Sandbox Software** V1.0. Nanjing University. **2015**  

---

{{< figure src="1.jpg" title="" >}}
{{< figure src="2.jpg" title="" >}}
{{< figure src="3.jpg" title="" >}}
{{< figure src="4.jpg" title="" >}}
{{< figure src="5.jpg" title="" >}}
{{< figure src="6.jpg" title="" >}}
{{< figure src="7.jpg" title="Partial PPT" >}}
{{< figure src="poster.jpg" title="Defense Poster" >}}

---

Translator: Ouyang Liujuan 
