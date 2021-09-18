# Generate node graph and line plots for the readme

pictures: nodes-4.png plot-10.png plot-100.png

nodes-4.png:
	./make-graph 4 | dot -Tpng > nodes-4.png

plot-10.png:
	./make-data 10 | gnuplot -e 'set terminal png; set output "plot-10.png"; plot "-" with lines title "10 nodes"' 


plot-100.png:
	./make-data 100 | gnuplot -e 'set terminal png; set output "plot-100.png"; plot "-" with lines title "100 nodes"' 

clean:
	-rm *.png
