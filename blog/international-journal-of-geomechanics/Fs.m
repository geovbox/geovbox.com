function dy = Fs(t,y,flag,havef,a,k,m,vis,applyF)
dy = zeros(2,1);    % a column vector
dy(1) = y(2) ;
dy(2) = havef * ( a- y(1)) * k / m  -  vis /m * y(2) - applyF/m;

%dy=zeros(2,1);
%dy(1)=y(2);
%dy(2)=1000*(1-y(1)^2)*y(2)-y(1);