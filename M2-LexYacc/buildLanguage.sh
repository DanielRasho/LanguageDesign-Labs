#!/bin/bash
flex ./simple_language.l
yacc -dtv ./simple_language.y
g++ -c lex.yy.c 
g++ -c y.tab.c
g++ -o calc y.tab.o lex.yy.o
