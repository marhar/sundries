%{
#include <stdio.h>
#include "y.tab.h"
#ifdef DUMPLEX
void show(char *s) { printf("%s(%s)\n",s, yytext); }
void shown() { printf("\n"); }
#else
void show(char *s) {}
void shown() {}
#endif
%}
%%
\{			{ show("LBRACE"); return LBRACE; }
\}			{ show("RBRACE"); return RBRACE; }
\[			{ show("LBRACKET"); return LBRACKET; }
\]			{ show("RBRACKET"); return RBRACKET; }
[(]			{ show("LPAREN"); return LPAREN; }
[)]			{ show("RPAREN"); return RPAREN; }
\.\.\.			{ show("DOTDOTDOT"); return DOTDOTDOT; }
[^ \t\n()\[\]{}]+	{ show("WORD"); return WORD; }
[\n]			{ shown(); return NEWLINE; }
\"[^"]*\"		{ show("WORD"); return WORD; }
^#.*$			;
.			;
%%
/*
[ \t]+			{ show("WS"); }
*/
