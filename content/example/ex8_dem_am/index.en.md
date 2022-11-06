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
## evolutionary process

<h5> </h5>
{{< figure src="dem_am.gif" title="" width="800px" >}}
<center><h5>Unit (cm)<br><br>Tectonic evolution process(DEM)</h5></center>

{{< figure src="dem_and_am02.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am04.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am08.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am12.jpg" title="" width="600px" >}}
{{< figure src="dem_and_am16.jpg" title="" width="600px" >}}
<center><h5>The first one is deformation for the AM. The second is deformation for the DEM. The third is the distortional strain field for the DEM. The shear strain magnitude is shown by color intensity. Red denotes top to the right sense of shear, and blue denotes top to the left sense of shear.</h5></center>

## ZDEM script: 

1. Generate. [gen.py](gen.py) ：

    {{< include-code "gen.py" bash >}}

2. Push. [push.py](push.py) ：

    {{< include-code "push.py" bash >}}

## The quantitative method of the thrust wedge based on mesh (Data) 

{{% notice info %}}
Download：[analog model.7z](analog model.7z) 
{{% /notice %}}

The images of the analog model.



