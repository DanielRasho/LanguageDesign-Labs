%{
#include <iostream>
#include <string>
#include <map>
static std::map<std::string, int> vars;
inline void yyerror(const char *str) { printf("Error: %s\n", str); }
int yylex();
%}

%union { int num; std::string *str; }

%token<num> NUMBER
%token<str> ID
%type<num> expression
%type<num> assignment

%right '='
%left '+' '-'
%left '*' '/'

%%

program: statement_list
        ;

statement_list: statement
    | statement_list statement
    ;

statement: assignment
    | expression ':'          { std::cout << $1 << std::endl; }
    | error ':' {
        yyerror("Invalid Expresion!"); 
        yyclearin; 
    }
    ;

assignment: ID '=' expression
    { 
        printf("Assign %s = %d\n", $1->c_str(), $3); 
        $$ = vars[*$1] = $3; 
        delete $1;
    }
    ;

expression: NUMBER                  { $$ = $1; }
    | ID                            { $$ = vars[*$1];      delete $1; }
    | expression '+' expression     { $$ = $1 + $3; }
    | expression '-' expression     { $$ = $1 - $3; }
    | expression '*' expression     { $$ = $1 * $3; }
    | expression '/' expression     { 
      if ($3 == 0){
        yyerror("Cannot divide by zero");
        $$ = 0;
      } else {
        $$ = $1 / $3; 
      }
    }
    ;

%%

int main() {
    yyparse();
    return 0;
}
