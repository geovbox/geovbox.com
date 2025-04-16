---
title: Calibration of the discrete element method and modelling of shortening experiments (Data)
date: 2021-05-24
categories:
    - Paper
    - Data
    - Script
authors:
    - LI ChangSheng
slug: li2021en 
---
LI Changsheng, YIN Hongwei*, et al. (2021) Calibration of the discrete element method and modelling of shortening experiments. Front. Earth Sci. [doi: 10.3389/feart.2021.636512](https://doi.org/10.3389/feart.2021.636512)

Original Research: The discrete element method (DEM) is becoming widely accepted as an effective method of addressing tectonic problems in granular materials. It is capable of reproducing structures observed in the analogue model (AM). However, the previous experiments ...

Accepted on 05 May 2021
## Evolution Process

<h5> </h5>
{{< figure src="dem_am.gif" title="" width="800px" >}}
<center><h5>Unit (cm)<br><br>Tectonic Evolution Process(DEM)</h5></center>

{{< figure src="dem_and_am02.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am04.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am08.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am12.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am16.jpg" title="" width="600px" >}}
<center><h5>"The first image (AM) shows the physical model; the second image (DEM) shows the discrete element numerical simulation; the third image shows the DEM deformation strain diagram.</h5></center>

## ZDEM script: 

1. deposition process. [gen.py](gen.py) is as follows：

    {{< includecode "gen.py" bash >}}

2. push process. [push.py](push.py) is as follows：

    {{< includecode "push.py" bash >}}

## The quantitative method of the thrust wedge based on mesh (Data) 

> Download：[analogmodel.7z](analogmodel.7z) 

The images of the analog model.



