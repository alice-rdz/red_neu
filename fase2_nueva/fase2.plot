set key off
set term png
set output "fase2.png"
m1=0.92323435
m2=0.12964316
b1=0.89699721
b2=-0.83204292
c1= 0.1106657
c2= 0.64934236

neurona(x) = m1*x+b1

plot [-1:1][-1:1]neurona(x) with lines lw 3 lt 3 title "Condicion", ((m2 * x + b2)) with lines lw 1 lt 4 title "Neurona inicial",'11.txt' using 1:2 with points pt 7 lt 5 title "Unos correctos", '10.txt' using 1:2 with points pt 7 lt 3 title "Unos incorrectos", '00.txt' using 1:2 with points pt 7 lt 33 title "Menos unos correctos", '01.txt' using 1:2 with points pt 7 lt 7 title "Menos unos incorrectos"
