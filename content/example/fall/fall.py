######################################
# title: 自由落体
# date: 2017-04-28
# authors: 李长圣
# E-mail: sheng0619@163.com
# more info, see www.geovbox.com
#######################################
START ; 开始一个计算
BALL  ID=0  X=2.0  Y=0.5  RAD=0.5  COLOR=blue ;生成一个蓝色颗粒，圆心(2.0,0.5)，半径0.5
BALL  ID=1  X=2.0  Y=2.5  RAD=0.5  COLOR=red
PROP  DEN=1e3  FRIC=0.0  KN=10e6  KS=10e6  DAMP=0.1;密度DEM，摩擦系数FRIC，法向刚度KN，切向刚度KS，阻尼DAMP
FIX   x y spin      RANGE id=(0, 0) ;固定id=0的颗粒的x和y方向的运动，并且固定其角速度spin
SET   DT=2.5e-04  GRAVTIY=(0.0, -9.81) ; 时间步DT，GRAVITY重力加速度
SET   vtk 100 ; 设置每100步保存一次vtk格式的计算结果
CYC   20000 ; 计算20000步
