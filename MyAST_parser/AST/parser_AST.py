from TokenType import TOKEN_TYPES_LIST
from treelib import Tree
from lexer import lexer
import re
import numpy as np
from AST.Trees import Treenodes
import uuid

STRING = ""


class parser_express:
    tree = Tree()
    lexem_mass = []
    varuable_items = []
    varuable_func = []
    pos = 0

    #  result = re.search(regex,str)
    def __init__(self, lex):
        self.lexem_mass = lex

    def Ismatch(self, mas):  # В текущей позиции указателя
        if len(self.lexem_mass) == self.pos:
            return False
        for i in mas:
            if self.lexem_mass[self.pos].text == i:
                return True
        return False

    def Match(self, mas):
        if len(self.lexem_mass) == self.pos:
            return False
        for i in mas:
            if self.lexem_mass[self.pos].text == i:
                self.pos += 1
                return i
        raise ValueError('Na pozicii', self.pos, 'obnaruzena oshibka')

    def number(self):
        self.pos += 1
        return self.lexem_mass[self.pos - 1].text

    def group(self):
        if (self.Ismatch(["("])):
            self.Match(["("])
            result = self.add()
            self.Match([")"])
            return result
        else:
            return self.number()

    def mult(self):
        result = self.group()
        while (self.Ismatch(["*", "/"])):
            oper = self.Match(["*", "/"])
            temp = self.group()
            result = Treenodes(oper, result, temp, self.pos)

        return result

    def add(self):
        result = self.mult()

        while (self.Ismatch(["+", "-"])):
            oper = self.Match(["+", "-"])
            temp = self.mult()

            result = Treenodes(oper, result, temp, self.pos)

        return result

    def start_expres_pars(self):
        result = self.add()
        return result

    def IsMatchRegex(self, regex):
        result = re.search(regex, self.lexem_mass[self.pos].text)
        if result is None:
            return False
        return True

    def identifierMatch(self, regex):
        result = re.search(regex, self.lexem_mass[self.pos].text)
        if result is None:
            raise ValueError('Na pozicii', self.pos, 'obnaruzena oshibka')
        self.pos += 1
        return result.group(0)

    def assign_varuable(self):

        result = self.identifierMatch(r'^[A-Za-z_]+')
        if (result in self.varuable_items):
            oper = self.Match(["="])
            result = Treenodes(oper, result, self.start_expres_pars(), self.pos)
            return result
        raise ValueError('Na pozicii', self.pos, 'Varuable not definded')

    def declaration(self):
        type = self.Match(["int", "void"])
        result = self.identifierMatch(r'^[A-Za-z_]+')
        self.varuable_items.append(result)
        if (self.Ismatch(["="])):
            oper = self.Match(["="])
            result = Treenodes(oper + " " + "declaration " + type, result + " varuable", self.start_expres_pars(), self.pos)
            return result


        result = Treenodes("declaration " + type, result + " varuable", None, self.pos)
        result.get().show()
        return result


    def reloop(self):
        result = self.Match(["<", ">", "==", "!="])
        return result;

    def bool_expression(self):
        result = []
        if (self.IsMatchRegex(r'^[0-9]+')):
            result = self.number()
        else:
            result = self.identifierMatch(r'^[A-Za-z_]+')
        oper = self.reloop()
        temp = self.identifierMatch(r'^[A-Za-z_]+')
        result = Treenodes(oper, result, temp, self.pos)
        return result

    def condition(self,cond):
        oper = self.Match([cond])
        self.Match(["("])
        result = self.bool_expression()
        self.Match([")"])
        return result

    def declarition_for(self):
        oper = self.Match(["for"])
        self.Match(["("])
        result = self.declaration()
        self.Match([";"])
        temp = self.bool_expression()
        self.Match([";"])
        self.Match([")"])
        return Treenodes("for_condition", result, temp, self.pos)

    def statement(self):

        result_tree = Tree()
        parent = str(uuid.uuid4())
        result_tree.create_node("body", parent)

        while (self.Ismatch(["int", "void", "bool", "{", "if", "for"]) or self.IsMatchRegex(r'^[A-Za-z_]+')):
            if (self.Ismatch(["int", "void"])):
                result_tree.paste(parent, self.declaration().get())
                self.Match([";"])
                continue
            if (self.Ismatch(["{"])):
                self.Match(["{"])
                result = self.statement()
                self.Match(["}"])
                return result
            if (self.Ismatch(["for"])):
                for_body = str(uuid.uuid4())
                result_tree.create_node("for-body", for_body, parent)
                result_tree.paste(for_body, self.declarition_for().get())
                result_tree.paste(for_body, self.statement())
                continue
            if (self.Ismatch(["if"])):
                if_body = str(uuid.uuid4())
                result_tree.create_node("if-body", if_body, parent)
                result_tree.paste(if_body, self.condition("if").get())
                result_tree.paste(if_body, self.statement())
                if(self.Ismatch(["else if"])):
                    elseif_body = str(uuid.uuid4())
                    result_tree.create_node("else if-body", elseif_body, parent)
                    result_tree.paste(elseif_body, self.condition("else if").get())
                    result_tree.paste(elseif_body, self.statement())
                    else_ = str(uuid.uuid4())
                    self.Match(["else"])
                    result_tree.create_node("else", else_, parent)
                    result_tree.paste(else_, self.statement())
                if(self.Ismatch(["else"])):
                    else_ = str(uuid.uuid4())
                    result_tree.create_node("else", else_, parent)
                    result_tree.paste(else_, self.statement())
                continue
            if (self.IsMatchRegex(r'^[A-Za-z_]+')):
                result_tree.paste(parent, self.assign_varuable().get())
                self.Match([";"])
                continue
        return result_tree

    def program_definded(self):
        result_tree = Tree()
        parent = str(uuid.uuid4())
        self.Match(["int","void"])
        func = self.identifierMatch(r'^[A-Za-z_]+')
        self.varuable_func.append(func)
        self.Match(["("])
        self.Match([")"])
        self.Match(["{"])
        result = self.statement()
        self.Match(['}'])
        result_tree.create_node(func,parent)
        result_tree.paste(parent,result)
        return result_tree


    def start_pars(self):
        result = self.program_definded()
        result.show(key=False)
        # result = self.start_expres_pars()
        # result.get().show()
