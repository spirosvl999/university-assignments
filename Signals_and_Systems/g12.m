t=-0.1:.001:0.1; %The requested time signal interval and its step 0.001 sec)
z=cos(100*pi*t)+ cos(200*pi*t)+sin(500*pi*t);%The Signal
figure('Name','Signal Creation');
plot(t,z);
legend('x(t)');
grid on;
ylabel('x(t)');
xlabel('Time');
TITLE('G.1.2');