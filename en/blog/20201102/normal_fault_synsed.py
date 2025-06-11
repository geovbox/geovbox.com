######################################
# title: 正断层
# date: 2020-10-30
# authors: 李长圣，徐雯峤
# E-mail: sheng0619@163.com
# 正断层上盘向右下角45度方向移动
# more info, see www.geovbox.com
#######################################
start
SET disk 0
BOX left 1.0e-3 right 25000.0 bottom 1.0e-3 height 20000.0 kn=4e10 ks=4e10 fric 0.30 

WALL id 0, nodes ( 1000.0 ,   4000.0 ) (   9000.0 ,  4000.0 ), kn=0e10 ks=0e10 fric 0.3 color black
WALL id 1, nodes ( 9000.0 ,   4000.0 ) (  21000.0 ,  4000.0 ), kn=0e10 ks=0e10 fric 0.3 color blue
WALL id 2, nodes ( 9000.0 ,   4000.0 ) (  13000.0 ,     0.0 ), kn=0e10 ks=0e10 fric 0.0 color blue

WALL id 3, nodes (  1000.0 ,   18000.0 ) (   1000.0 ,  4000.0 ), kn=0e10 ks=0e10 fric 0.3 color black
WALL id 4, nodes ( 21000.0 ,   4000.0 ) (  21000.0 ,  18000.0 ), kn=0e10 ks=0e10 fric 0.3 color black

gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 21000.0, y 4000.0, 18000.0, GROUP ball_rand
prop color black den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz

SET STEPBAR  1000
set print 5000
SET DT 5e-2,     
SET GRAVITY ( 0.0,  -10.0 )

CYC  10000
DEL  range y 10000.0, 20000.0
CYC  5000
DEL  range y 10000.0, 20000.0
CYC  5000
exp  initxyr.dat range group ball_rand
SAV  initxyr.sav

prop color mg     range group ball_rand
prop color green  range y  4000.0  5000.0
prop color green  range y  6000.0  7000.0
prop color green  range y  8000.0  9000.0
prop color green  range y  10000.0 99999.0

prop fric 0.3 range group ball_rand
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 

################################### sed1-1 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 21200.0, y 8000.0, 10000.0, GROUP sed1
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed1
set print -1
CYC  10000
prop fric 0.3 range group sed1
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 
################################### sed1-2 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 21400.0, y 8000.0, 10000.0, GROUP sed1
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed1
set print -1
CYC  10000
prop fric 0.3 range group sed1
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 
################################### sed1-3 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 21600.0, y 8000.0, 10000.0, GROUP sed1
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed1
set print -1
CYC  10000
prop fric 0.3 range group sed1
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 
################################### sed1-4 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 21800.0, y 8000.0, 10000.0, GROUP sed1
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed1
set print -1
CYC  10000
prop fric 0.3 range group sed1
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 
################################### sed1-5 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 22000.0, y 8000.0, 10000.0, GROUP sed1
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed1
set print -1
CYC  10000
prop fric 0.3 range group sed1
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0 


################################### sed2-1 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 22200.0, y 8000.0, 10000.0, GROUP sed2
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed2
set print -1
CYC  10000
prop fric 0.3 range group sed2
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed2-2 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 22400.0, y 8000.0, 10000.0, GROUP sed2
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed2
set print -1
CYC  10000
prop fric 0.3 range group sed2
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed2-3 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 22600.0, y 8000.0, 10000.0, GROUP sed2
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed2
set print -1
CYC  10000
prop fric 0.3 range group sed2
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed2-4 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 22800.0, y 8000.0, 10000.0, GROUP sed2
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed2
set print -1
CYC  10000
prop fric 0.3 range group sed2
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed2-5 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 23000.0, y 8000.0, 10000.0, GROUP sed2
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed2
set print -1
CYC  10000
prop fric 0.3 range group sed2
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0

################################### sed3-1 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 23200.0, y 8000.0, 10000.0, GROUP sed3
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed3
set print -1
CYC  10000
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed3-2 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 23400.0, y 8000.0, 10000.0, GROUP sed3
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed3
set print -1
CYC  10000
prop fric 0.3 range group sed3
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed3-3 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 23600.0, y 8000.0, 10000.0, GROUP sed3
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed3
set print -1
CYC  10000
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed3-4 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 23800.0, y 8000.0, 10000.0, GROUP sed3
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed3
set print -1
CYC  10000
prop fric 0.3 range group sed3
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed3-5 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 24000.0, y 8000.0, 10000.0, GROUP sed3
prop color blue den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed3
set print -1
CYC  10000
prop fric 0.3 range group sed3
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0


################################### sed4-1 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 24200.0, y 8000.0, 10000.0, GROUP sed4
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed4
set print -1
CYC  10000
prop fric 0.3 range group sed4
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed4-2 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 24400.0, y 8000.0, 10000.0, GROUP sed4
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed4
set print -1
CYC  10000
prop fric 0.3 range group sed4
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed4-3 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 24600.0, y 8000.0, 10000.0, GROUP sed4
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed4
set print -1
CYC  10000
prop fric 0.3 range group sed4
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed4-4 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 24800.0, y 8000.0, 10000.0, GROUP sed4
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed4
set print -1
CYC  10000
prop fric 0.3 range group sed4
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0
################################### sed4-5 ######################################
wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
gen NUM 100000, rad discrete 60.0 80.0,  x 1000.0, 25000.0, y 8000.0, 10000.0, GROUP sed4
prop color gb den 2.5e3, fric 0.0, shear 2.8e9, poiss 0.2, damp 0.4, hertz,range GROUP sed4
set print -1
CYC  10000
prop fric 0.3 range group sed4
wall id 1 xv 2.0, yv -2.0  
wall id 4 xv 2.0, yv -2.0
imple wall id 4 xmove 200.0 print 100.0

wall id 1 xv 0.0, yv -0.0  
wall id 4 xv 0.0, yv -0.0
CYC 5000
STOP

