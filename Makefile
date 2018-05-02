pictures: 
	for N in 1 2 8; do			\
	  ./make-graph $$N > N$$N.gv;		\
	  dot -Tpng N$$N.gv > N$$N.png;		\
	done	

clean:
	-rm *.gv *.png
