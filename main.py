# This is a sample Python script.
import re
import numpy as np
from treelib import Tree
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lexer import lexer
import sys

from AST.parser_AST import parser_express
from AST.Trees import Treenodes


# code = "void foo(a,b){\n return a + b;}"
# code = "5+3*(4+7)+3*2"
code = "int main () { \n" \
       "int a = 10;\n" \
       "if(15 == a){\n" \
       "a = 20;}\n" \
       "else if (15 < a){\n" \
       "a = 15;}\n"\
       "else {\n" \
       "a = 0;}" \
       "for(int i = 0; 10 < i;){\n" \
       "int b = 56+23*(32+2+1)-5;\n i = i + 1;\n}}" \

# code = "int abc = 5;\n if ( 2 < abc) {int bc = 1;\n if(2 > abc) {int k = 20+5*(3+4);}}"
# code = "int abc = 5; for(int i = 0; 10 > i; ) \n {int b = 5+3*(2+5);}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    l1 = lexer(code)
    l1.lexAnalysis()
    token_list = np.array(l1.tokenList)
    ast = parser_express(token_list)
    ast.start_pars()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
