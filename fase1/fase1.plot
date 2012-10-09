set key off
set term png
set output "fase1.png"
plot 'unos.txt' u 1:2 w points pt 5 lt 1, 'ceros.txt' u 1:2 w point pt 7 lt 3

