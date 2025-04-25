---
title: Discrete Element Post-processing Techniques and Their Applications in Structural Simulation (Preview)
date: 2021-10-31
categories:
    - Thesis
    - Master
    - Report
authors:
    - HuajingWei 
images:
    - 3.png
slug: 20221031
---

Recently, we will invite Wei Huajing, a master's student from Nanjing University, to present his research findings on discrete element post-processing, DEMpost. Teachers and students who are interested can download Wei Huajing's master's thesis for study first. The report time will be notified separately.
#### Thesis download

1. [**HuajingWei** (2020) Discrete Element Post-processing Techniques and Their Applications in Structural Simulation. **Master's Thesis**. Nanjing University.](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFDTEMP&filename=1021664929.nh&uniplatform=NZKPT&v=e5D04YZeOE6krJkFB%25mmd2BA6u8bMwzx%25mmd2FkyJjqC4HZrX6jLBHP44DVzv%25mmd2BkoQw0Xl8MjYl) 

#### Title: Quantitative Analysis and Simulation of Structural Deformation in Fold-Thrust Belts Based on Discrete Element Method
#### Author: Wei Huajing
#### Recommendation Reason
The discrete element post-processing program DEMpost developed in this paper can extract the stratum boundaries of particle systems, outline the scope of specific rock layers, and draw various cloud diagrams such as stress-strain, velocity, and displacement fields. It is an indispensable tool for quantitative research on structural deformation.
{{< figure src="1.png" title="Extract stratum boundaries" >}}
{{< figure src="2.png" title="Identify salt layer extent" >}}
{{< figure src="3.png" title="Plot stress-strain" >}}

#### Abstract
The discrete element method (DEM) is a numerical simulation technique that uses a microscopic particle system to simulate the deformation of macroscopic objects. It is widely applied in fields such as geotechnical engineering, structural simulation, and material transport. As an important means of quantitative structural research, structural numerical simulation establishes a connection between deformation mechanisms and geometric analysis of structures, overcoming the limitations of traditional structural analysis methods in the study of salt-bearing fold-thrust belts to a certain extent. DEM numerical simulation can present structural deformation and track the force and motion states of particles at each moment during the simulation, providing information on the stress-strain state and velocity-displacement field of the system. This allows for the study of small-scale deformations and fractures, enabling quantitative research on salt-bearing fold-thrust structures with significant scientific and economic value. Therefore, efficiently expressing the distribution of dynamic and kinematic characteristics in structural simulations has important application value. Based on literature research, algorithm design and development, computational examples, and structural numerical simulation experiments, this paper has completed the following work:

1.The literature review discusses the importance of multi-dimensional post-processing analysis for structural simulation: while structural deformation reflects the overall shape of the structure, the distribution of strain can reflect small-scale structural deformation in the model, the distribution of velocity fields can reveal the motion states of different structural units, and displacement gradients can provide a more detailed view of fracture distribution.
2.Designed and developed a post-processing calculation and visualization analysis module DEMpost adapted to the discrete element software YADE. The particle system is presented in the form of images through a rasterization algorithm, and the stress-strain and other characteristics of the particle system are presented in the form of images through an inverse distance weighted interpolation algorithm. The quality of these images is improved through other image processing algorithms. An association can be established between the structural deformation images in image form and the characteristic maps, facilitating the tracking of dynamic and kinematic characteristics of specific structural units during structural evolution.
3.Designed systematic discrete element numerical simulation experiments, analyzed the influence of common factors in salt-bearing fold-thrust belt structures, realized post-processing visualization of structural simulation based on DEMpost, and explored the mapping relationship between structural deformation and dynamic and kinematic characteristics. The simulation results show that the presence of a single gypsum-salt layer at the bottom causes stress-strain to rapidly propagate to the structural boundary, resulting in contraction and extrusion within the entire model and the development of a "box-like" structure; the presence of double gypsum-salt layers transforms rigid uplift associated with conjugate faults into a rheological fold structure, with stable stress-strain states within the gypsum-salt layers, and their influence on the structure is manifested as strain dispersion and triangular shear zones with a certain radiation range; pre-existing faults promote upward movement of the hanging wall along the fault, and factors such as the dip direction, dip angle, and scale of pre-existing faults affect the direction and distance of hanging wall movement, which in turn affects the range of deformation propagation.

#### Keywords: discrete element method; post-processing; rasterization; spatial interpolation; image processing; structural numerical simulation; quantitative analysis
#### Contents:

1. Introduction 
    + 1.1 Quantitative Research on Fold-Thrust Belts and Structural Analysis 
    + 1.2 Introduction to Discrete Element Software
    + 1.3 Summary of This Paper
    + 1.4 Research Methods and Technical Routes
    + 1.5 Workload of the Thesis
2. Algorithm Design and Development of Discrete Element Post-processing Techniques
    + 2.1 Data Preprocessing
    + 2.2 Discrete Element Imaging
        - 2.2.1 Structural Deformation Images
        - 2.2.2 Dynamic and Kinematic Characteristic Maps
    + 2.3 Image Enhancement Processing
        - 2.3.1 High-Frequency Noise Suppression
        - 2.3.2 Region Boundary Extraction
        - 2.3.2 System Outline Expression
    + 2.4 Summary
3. Computational Examples and Advantages of Discrete Element Post-processing Techniques
    + 3.1 Computational Examples of Discrete Element Post-processing Algorithms
    + 3.2 Advantages of Discrete Element Post-processing Algorithms
    + 3.3 Summary
4. Application of Discrete Element Post-processing Techniques in Salt-Bearing Fold-Thrust Belt Structural Simulation 
    + 4.1 Single Gypsum-Salt Layer
    + 4.2 Double Gypsum-Salt Layers 
        - 4.2.1 Vertical Scale of Gypsum-Salt Layers
        - 4.2.2 Lateral Scale of Gypsum-Salt Layers
        - 4.2.3 Vertical Distribution of Gypsum-Salt Layers
        - 4.2.4 Lateral Distribution of Gypsum-Salt Layers
    + 4.3 Pre-existing Faults
        - 4.3.1 Dip Direction of Pre-existing Faults
        - 4.3.2 Dip Angle of Pre-existing Faults
        - 4.3.3 Vertical Distribution of Pre-existing Faults
        - 4.3.4 Lateral Distribution of Pre-existing Faults
        - 4.3.5 Scale of Pre-existing Faults
    + 4.4 Summary
5. Conclusions and Future Directions
    + 5.1 Conclusions
    + 5.2 Future Directions 


---

Translator: Ouyang Liujuan 