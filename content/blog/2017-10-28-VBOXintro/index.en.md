---
title: VBOX overview
date: 2017-10-28
categories:
    - Software
authors:
    - LiChangsheng
images:
    - VBOX_GUI.png
slug: VBOX-overview
---

> Download：[VBOX Brief introduction](VBOX-overview.pdf)

VBOX (Virtual Sandbox) is a 2D Discrete Element Method (DEM) software platform specifically designed for tectonic deformation research. Developed in 2014 using C language with OpenMP parallelization, this copyrighted system addresses critical limitations of analog sandbox experiments in stress-strain quantification and material rheology representation, providing a novel computational approach for structural geology studies.

The software suite and technical documentation will undergo progressive enhancements, with updates to be released incrementally. Please stay tuned for forthcoming developments！


VBOX(virtual sandbox) is a 2D DEM program to simulate the geological problems. It is developed by C-language. We takes  three years  to construct the new data structure and neighbor search algorithm based on grid for VBOX. Furthermore, GUI was embeded into VBOX using [gtkmm](https://www.gtkmm.org/) [PLplot](http://plplot.sourceforge.net/) [Cairo](https://www.cairographics.org/)


The VBOX can perform angle of repose tests, direct shear tests, biaxial tests, and structural simulation tests, see download.

The desktop version of VBOX has been in development, and the preview version is shown in the image below:

{{< figure src="VBOX_GUI.png" title="VBOX desktop preview" >}}

VBOX can be implemented ``Angle of rest`` ``Direct shear test`` ``Biaxial test`` ``Construction simulation`` ：

{{< figure src="20171207-VBOX.png" title="VBOX overview" >}}



---

Translator: Chi Yu
