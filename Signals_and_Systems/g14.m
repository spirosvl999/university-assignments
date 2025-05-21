t=-0.1:.001:0.1;                                                    %The time interval of the requested signal and its step .001 sec)
z=cos(100*pi*t)+ cos(200*pi*t)+sin(500*pi*t);

Ts1=0.002;%We set Ts1=0.002 sec
N1=-50:1:50;
Xs1=cos(100*pi*N1*Ts1)+cos(200*pi*N1*Ts1)+sin(500*pi*N1*Ts1);    %The new signal with the same sampling frequency that we found in G.1.1
Ts2=0.0001;%We set a higher frequency to get a shorter period:f=10000 Hz
N2=-1000:1:1000;
Xs2=cos(100*pi*N2*Ts2)+cos(200*pi*N2*Ts2)+sin(500*pi*N2*Ts2);
for k=1:1:length(t)
    x1(k)=Xs1*sinc((t(k)-N1*Ts1)/Ts1)';
end;

for k=1:1:length(t)
   x2(k)=Xs2*sinc((t(k)-N2*Ts2)/Ts2)';
end;


figure('Name','Urgent Signal for Ts=0.0001');
hold on;

plot(t,z);                                                      %Display of the signal G.1.2
hold on;
plot(t,x1,'-r');                                                %Display of the signal G.1.3 
hold on;
plot(t,x2,'-g');                                                %Display of the signal G.1.4
legend('Xs(t)');
legend('y(t)');
TITLE ('G.1.4');
xlabel('Time');
ylabel('x1(t)');
grid on;
