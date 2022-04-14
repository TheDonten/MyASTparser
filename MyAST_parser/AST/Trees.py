
from treelib import Tree
import uuid

class Treenodes:

    tree = []

    def set(self, tree):
        self.tree = tree

    def get(self):
        return self.tree

    def __init__(self,operand,result,temp,pos):
        self.tree = Tree()
        parent = str(uuid.uuid4())
        if temp == None:
            self.tree.create_node(operand, parent)
            self.tree.create_node(result, str(uuid.uuid4()), parent=parent)
            return
        if isinstance(temp,Treenodes) and isinstance(result,Treenodes):

            self.tree.create_node(operand,parent)
            self.tree.paste(parent,result.get())
            self.tree.paste(parent,temp.get())

        elif isinstance(temp,Treenodes):
            self.tree.create_node(operand,parent)
            self.tree.create_node(result,str(uuid.uuid4()), parent= parent)
            self.tree.paste(parent,temp.get())

        elif isinstance(result,Treenodes):
            self.tree.create_node(operand, parent)
            self.tree.paste(parent, result.get())
            self.tree.create_node(temp, str(uuid.uuid4()), parent=parent)
        else:
            self.tree.create_node(operand, parent)
            self.tree.create_node(result, str(uuid.uuid4()), parent=parent)
            self.tree.create_node(temp, str(uuid.uuid4()), parent=parent)

    # def create_treend





