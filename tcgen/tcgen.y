%{
#include <stdio.h>
#include <string.h>
void yshow(char*s) {printf("->%s\n",s);}
%}
%token LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE WORD DOTDOTDOT NEWLINE
%%
top: entries;

entries: | entries entry;

entry:
	  clauses NEWLINE		{ yshow("entry"); }
	;

clauses:
	  /* empty */
	| clauses clause;
clause:
	  simpleclause
	| choiceclause
	| optionalclause
	| groupedclause
	;

simpleclause:
	  words
	;

choiceclause:
	  LBRACE clauses RBRACE		{ yshow("choiceclause"); }
	;

optionalclause:
	  LBRACKET clauses RBRACKET	{ yshow("optionalceclause"); }
	;

groupedclause:
	  LPAREN clauses RPAREN		{ yshow("groupedclause"); }
	;

words:
	  /* empty */
	| words WORD
	;

%%
void yyerror(const char *str)
{
        fprintf(stderr,"error: %s\n",str);
}
int yywrap()
{
        return 1;
} 
extern int yydebug;
main()
{
    printf("yydebug=%d\n",yydebug);
    yyparse();
} 
