######################################
# title: 基于离散元的挤压构造定量分析与模拟:1 沉积
# date: 2022-09-01
# authors: 李长圣
# E-mail: sheng0619@163.com
# ref: [李长圣,尹宏伟,徐雯峤,吴珍云,管树巍,贾 东,任 荣.基于离散元的挤压构造定量分析与模拟[J].大地构造与成矿学,2022,(46卷04):645-661.](https://doi.org/10.16539/j.ddgzyckx.2022.04.001) 
# more info, see www.geovbox.com
#######################################
start
set disk 0
BOX left 0.1 right 62000.0 bottom 1.0 height 20000.0 kn=4e10 ks=4e10 fric 0.00 
GLINE P1 (   1000.0 ,  1000.0 ) P2 (  61200.0 ,   1000.0 ) r 40.0 GROUP bom_wall
GLINE P1 (   1000.0 ,  1120.0 ) P2 (   1000.0 ,  19000.0 ) r 80.0 GROUP lef_wall
GLINE P1 (  61000.0 ,  1120.0 ) P2 (  61000.0 ,  19000.0 ) r 80.0 GROUP rig_wall

GEN num 200000, rad discrete 60.0 80.0,  x ( 1000 61000), y (1000 16000), COLOR black 
PROP den 2.5e3, fric 0.0, shear 2.9e9, poiss 0.2,  damp 0.4 hertz

prop color blue    range group bom_wall
prop color black   range group lef_wall
prop color black   range group rig_wall

fix x y  spin range group bom_wall
fix x y  spin range group lef_wall
fix x y  spin range group rig_wall

SET  DT 5e-2,  GRAVITY ( 0.0,  -9.8 )
PROP damp 0.4
DRAW INTERVAL 1000, bfill wall bondc ;,bid,bang  mesh, cforce

SET  stepbar  1000
SET  save    50000
set  print   1000
set  ps      1000

CYC 5000

del range x 1001 60999 y 7000 99999
CYC 5000
exp init6km_xyr.dat range x 1001.0 60999.0 y 1001.0 99999.0

del range x 1001 60999 y 6000 99999
CYC 5000
exp init5km_xyr.dat range x 1001.0 60999.0 y 1001.0 99999.0

stop