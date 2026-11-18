%2017-06-11 LI ChangSheng @ NanJing University
%E-mail: sheng0619@163.com
%ref.
%[1]LI ChangSheng, YIN HongWei. Validation tests for discrete element codes using single-contact systems
%T1 T2 T3 T4
%analytical solutions for the tests of the normal contact force and the shear contact force
%
%MATLAB R2015a, just run this code

clc
clear
kn  = 5.5e9;
den = 2.5e3;
rad = 50.0;
m   = den * 2.0 * sqrt(3) * rad^2;
%m=2.1651e+07;
k   = sqrt(kn/m);
tbegin = 0.001;
tend   = 0.4;
%*************************************************************************
%T1 T2
subplot(1,2,1)
%draw y=0.0
plot([0.0 tend],[0.0 0.0],'k-.');
hold on;
%particle1 particle2 position and rad
% (0,0) 50    (0,50) 50
% particle2 initial velocity (0.0, -1e-1)
vel   = -1e-1; 

%T1 
%without viscosity 0.0
vis   = 0.0;
n     = vis/m/2.0;
omega = sqrt(k^2-n^2);
tn1=pi/omega; % exact value 0.2189
tn1int   = 0.197; % for int value 0.197/dt= 197,note dt = 0.001
A     = vel/omega;

%see paper[1] Table2 T1 eq13 
%[0, t_n1) 
tn01  = [0.001:0.001:tn1int];
yn01  = A.*exp(-n.*tn01).*sin(omega.*tn01);
%plot(tn01,yn01,'r-')
velend = -A*omega;

%see paper[1] Table2 T1 eq14 
%[t_n1,0.4) 
tn1end = [tn1int+0.001:0.001:tend];
yn1end = velend.*(tn1end-tn1);

tnvis0 = [tn01 tn1end]';
ynvis0 = [yn01 yn1end]';
plot(tnvis0,ynvis0,'r-')

%T2
%viscosity 3e8
%tend=2*pi/omega;
vis    = 3e8;
n      = vis/m/2.0;
omega  = sqrt(k^2-n^2);
tn2       = pi/omega; % exact value 0.2189
tn2int    = 0.218;    % for int value 0.218/dt= 197,note dt = 0.001
tn02   = [tbegin:0.001:tn2int];
A      = vel/omega;

%see paper[1] Table2 T2 eq15 
%[0, t_n2)
yn02   = A.*exp(-n.*tn02).*sin(omega.*tn02);
vel2   = -A*omega*exp(-n*pi/omega);

tn2end = [tn2int+0.001:0.001:tend];
C2     = vel2/(-2*n*exp(-2*n*tn2));
C1     = -C2*exp(-2*n*tn2);
y2end  = C2.*exp(-2*n.*tn2end)+C1;

%see paper[1] Table2 T2 eq16 
%[t_n2,0.4)
tnvis3 = [tn02 tn2end]';
ynvis3 = [yn02 y2end]';

plot(tnvis3, ynvis3,'b-')
legend('y=0','T1 vis=0','T2 vis=3e8');
xlabel('t(s)')  
ylabel('Particle2''s y-position (m)')
title('Analytical solution')

%*************************************************************************
%T3 T4
%analytical solutions for the tests of the shear contact force
%
% wall3 nodes (0.220573 100.0) (0.220573 -100.0)    
% particle4 position and rad (50,0) 50
clc
clear
subplot(1,2,2)
ks  = 5.5e9;
kn  = ks;
den = 2.5e3;
rad = 50.0;
m   = den * 2.0 * sqrt(3) * rad^2;
k   = sqrt(ks/m);
tbegin = 0.001;
tend   = 0.4;
% particle4 initial velocity (0.0, 1.0)
v0    = 1;

% T4
% viscosity
vis=3e8;
n     = vis/m/2.0;
omega = sqrt(k^2-n^2);
A     = v0/omega;
%1.  first  segment
%see paper[1] Table3 T4 eq20 
%[0, t_s2)
ts2     = pi/(8.0*omega);     % exact value 0.027358375988797
ts2int  = 0.027;  % for int value
ts02 = [tbegin:0.001:ts2int]; 
ys02  = A.*exp(-n.*ts02).*sin(omega.*ts02);
%plot(ts02,ys02,'b-')
hold on
y0 = A*exp(-n*ts2(end))*sin(omega*ts2(end));
%plot(ts2,y0,'r*');
vs2 = ( (-n)*sin(omega*ts2) + omega*cos(omega*ts2) )*A*exp(-n*ts2);

%2.  second  segment
%see paper[1] Table3 T4 eq21
%[t_s2,t_s4)
Fsmax    = ks*y0;
g        = Fsmax/m;
friction = 0.1;
Fn       = Fsmax /friction;
xn       = Fsmax/friction/kn;

C2 = (vs2+g/(2.0*n))/(-2*n*exp(-2*n*ts2));
C1 = y0+g/(2*n)*ts2-C2*exp(-2*n*ts2);
ys2 = C1+C2*exp(-2*n*ts2)-g/(2*n)*ts2;
%plot(ts2,ys2,'ro')

ts3     = (-1/(2*n)) * log( g/(2*n)/(C2*(-2*n)) ) ;% 0.093910070513473
ts3int  = 0.093;
ts23   = [ts2int+0.001:0.001:ts3int];
ys23   = C1+C2*exp(-2*n.*ts23)-g/(2*n).*ts23;
%plot(ts23,ys23,'b-.');
ys3     = C1+C2*exp(-2*n*ts3)-g/(2*n)*ts3;
%plot(ts3,ys3,'ro');

%3.  third  segment
%see paper[1] Table3 T4 eq22
%[t_s4,t_end)
a=ys3-ys2; %equilibrium position moves up to (ys2-ys1)
[ts3end,ys3end] = ode15s('Fs',[ts3int+0.001:0.001:tend],[ys3 0.0],[],1.0,a,kn,m,vis,0.0);
%plot(ts3end,ys3end(:,1),'r-')
%scatter(ts3end,ys3end(:,1),'r');

tsvis3 = [ts02 ts23 ts3end']';
ysvis3 = [ys02 ys23 ys3end(:,1)']';
plot(tsvis3,ysvis3,'b-')
hold on

% T3
% without viscosity
vis=0.0;
n=vis/m/2.0;
k=sqrt(ks/m);
omega = sqrt(k^2-n^2);
A=v0/omega;

Fsmax = ks*y0;%y0 same as T4, maximum shear force is same with T4, particle4 slip in y0
g     = Fsmax/m;
xn    = Fsmax/friction/kn;
v0    = v0;% initial velocity same as T4

%1.  first  segment
%see paper[1] Table3 T3 eq17 
%[0, t_s1)
ts1    = 1/omega * asin(y0/A) ;% 0.022538940308419
ts1int = 0.022;
ts01   = [0.001:0.001:ts1int];
ys01    = A.*exp(-n.*ts01).*sin(omega.*ts01);
%plot(ts01,ys01,'r-')

ys1 = A * sin(omega*ts1);
vs1 = A * omega * cos(omega*ts1);
%plot(ts1,ys1,'b*');
C1     = vs1+g*ts1;
C2     = ys1+g*ts1^2/2.0 - C1*ts1;
ts4    = (-C1)/(-g); %0.189612878190028
ts4int = 0.189;

%2.  second  segment
%see paper[1] Table3 T4 eq18
%[t_s1,t_s4)
ts14 =[ts1int+0.001:0.001:ts4int];
ys14 = - g*ts14.*ts14 /2 + C1.*ts14 +C2;
%plot(ts14,ys14,'r-.')
ys1_ = -g*ts1*ts1/2 + C1*ts1 +C2;
%plot(ts1,ys1_,'ro')
y4 = - g*ts4*ts4 /2 + C1*ts4 +C2;
%plot(ts4,y4,'ro')

%3.  third  segment
%see paper[1] Table3 T3 eq19
%[t_s4,t_send)
phi    = pi/2;
A      = sqrt(y0^2); % amplitude change to y0 , i.e. max shear displacement before slide
addy   = y4-A.*exp(-n*ts4).*sin(omega*ts4+pi/2-omega*ts4);
y1_4   = y4-ys1_;
ts4end = [ts4int+0.001:0.001:tend];
ys4end = A.*exp(-n.*ts4end).*sin(omega.*ts4end+pi/2-omega*ts4)+addy;
%plot( ts4end,ys4end,'r-')
tsvis0   = [ts01 ts14 ts4end]';
ysvis0   = [ys01 ys14 ys4end]';
plot(tsvis0,ysvis0,'r-')
%scatter(tsvis0,ysvis0,'r');


set(gca,'box','on')
legend('T4 vis=3e8','T3 vis=0e8');
xlabel('t(s)')  
ylabel('Particle4''s y-position (m)')
title('Analytical solution')
