t=-0.1:.001:0.1;%The time interval of the requested signal and its step of .001 sec)
Ts=0.002;%We set Ts=0.002 sec
N1=-50:1:50;
z=cos(100*pi*t)+ cos(200*pi*t)+sin(500*pi*t);%The given signal
Xs=cos(100*pi*N1*Ts)+cos(200*pi*N1*Ts)+sin(500*pi*N1*Ts);%The new Signal we found.
for k=1:1:length(t)
    x1(k)=Xs*sinc((t(k)-N1*Ts)/Ts)';
end;
figure('Name','New Signal for Ts=0.002');
hold on;
%Show Signals:
plot(t,z);%Show of signal G.1.2
plot(t,x1,'-r');%Show of G.1.3 signal with G.1.2
legend('Xs(t)');
legend('y(t)');
TITLE ('G.1.3');
xlabel('Time');
ylabel('x1(t)');
grid on;