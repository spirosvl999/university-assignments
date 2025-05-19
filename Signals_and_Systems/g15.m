t=-0.1:.001:0.1;
z=cos(100*pi*t)+ cos(200*pi*t)+sin(500*pi*t);

Ts1=0.002;
N1=-50:1:50;
Xs1=cos(100*pi*N1*Ts1)+cos(200*pi*N1*Ts1)+sin(500*pi*N1*Ts1);

Ts2=0.0001;
N2=-1000:1:1000;
Xs2=cos(100*pi*N2*Ts2)+cos(200*pi*N2*Ts2)+sin(500*pi*N2*Ts2);

Ts3=0.02;
N3=-5:1:5;
Xs3=cos(100*pi*N3*Ts3)+cos(200*pi*N3*Ts3)+sin(500*pi*N3*Ts3);

for k=1:1:length(t)
    x1(k)=Xs1*sinc((t(k)-N1*Ts1)/Ts1)';
end;


for k=1:1:length(t)
    x2(k)=Xs2*sinc((t(k)-N2*Ts2)/Ts2)';
end;

for k=1:1:length(t)
    x3(k)=Xs3*sinc((t(k)-N3*Ts3)/Ts3)';
end;



figure('Name','Reconstructed Signal for Ts=0.02');
hold on;

plot(t,z);%G.1.2
hold on;
plot(t,x1,'-r');%G.1.3 
hold on;
plot(t,x2,'-g');%G.1.4
hold on;
plot(t,x3,'-m');%G.1.5
legend('Xs(t)');
legend('y(t)');
TITLE ('G.1.5');
xlabel('Time');
ylabel('x1(t)');
grid on;