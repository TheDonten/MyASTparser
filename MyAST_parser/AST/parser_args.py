from TokenType import TOKEN_TYPES_LIST
from treelib import Tree
from lexer import lexer
import re
import numpy as np
from AST.Trees import Treenodes

class parser_arg:

    tree = Tree()
    lexem_mass = []
    pos = 0

    def Ismatch(self, mas):    #В текущей позиции указателя
        if len(self.lexem_mass) == self.pos:
            return False
        for i in mas:
            if self.lexem_mass[self.pos].text == i:
                return True
        return False

    def Match(self,mas):
        if len(self.lexem_mass) == self.pos:
            return False
        for i in mas:
            if self.lexem_mass[self.pos].text == i:
                self.pos += 1
                return i
        raise ValueError('Na pozicii', self.pos, 'obnaruzena oshibka')