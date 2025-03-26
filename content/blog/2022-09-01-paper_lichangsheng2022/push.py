######################################
# title: 基于离散元的挤压构造定量分析与模拟:2 挤压
# date: 2022-09-01
# authors: 李长圣
# E-mail: sheng0619@163.com
# ref: [李长圣,尹宏伟,徐雯峤,吴珍云,管树巍,贾 东,任 荣.基于离散元的挤压构造定量分析与模拟[J].大地构造与成矿学,2022,(46卷04):645-661.](https://doi.org/10.16539/j.ddgzyckx.2022.04.001) 
# more info, see www.geovbox.com
#######################################
load init5km_xyr.dat

set disk 0
BOX left 0.1 right 62000.0 bottom 1.0 height 20000.0 kn=4e10 ks=4e10 fric 0.00 
GLINE P1 (   1000.0 ,  1000.0 ) P2 (  61200.0 ,   1000.0 ) r 40.0 GROUP bom_wall
GLINE P1 (   1000.0 ,  1120.0 ) P2 (   1000.0 ,  19000.0 ) r 80.0 GROUP lef_wall
GLINE P1 (  61000.0 ,  1120.0 ) P2 (  61000.0 ,  19000.0 ) r 80.0 GROUP rig_wall

PROP color white den 2.5e3, fric 0.0, shear 2.9e9, poiss 0.2, hertz

prop color blue    range group bom_wall
prop color black   range group lef_wall
prop color black   range group rig_wall
fix x y   spin range group bom_wall
fix x y   spin range group lef_wall
fix x y   spin range group rig_wall

SET  DT 5e-2,  GRAVITY ( 0.0,  -9.8 )
PROP damp 0.4

SET  stepbar  1000
set  print    5000
set  ps       5000

prop   ebmod 2e8 gbmod 2e8 tstrength 1e7 sstrength 2e7 fric 0.3 range x 1001.0 60999.0 y 1001.0  9000.0
prop color mg     range x 1001.0 60999.0 y 1700.0  2000.0
prop color violet range x 1001.0 60999.0 y 2700.0  3000.0
prop color green  range x 1001.0 60999.0 y 3700.0  4000.0
prop color blue   range x 1001.0 60999.0 y 4700.0  5000.0
prop color black  range x 1001.0 60999.0 y 5700.0  9000.0

prop color blue   fric 0.3 range group lef_wall
prop color blue   fric 0.3 range group rig_wall
prop color red    fric 0.3 range group bom_wall

ini  xv 2.0, range group lef_wall
wall id 1, nodes (  500.0 , 2000.0 )  (    500.0 ,   3000.0 ), kn=0e3 ks=0e3 color black fric 0.0  xv  2.0
imple wall id 1 xmove 20000 print 1000.0 ps 1000.0 vtk 1000.0 sav 2000.0
stop