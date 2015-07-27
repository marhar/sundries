all:
	lex tcgen.l
	yacc -vd tcgen.y
	cc -DYYDEBUG -DDUMPLEX lex.yy.c y.tab.c -o tcgen 

clean:
	rm -f lex.yy.c tcgen.tab.c tcgen.tab.h y.output y.tab.c y.tab.h

clobber: clean
	rm -f tcgen tstlex

tstlex: tcgen.l tcgen.y
	yacc -vd tcgen.y
	lex tcgen.l
	cc -DDUMPLEX lex.yy.c -o tstlex -ll

