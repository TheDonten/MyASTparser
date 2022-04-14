from TokenType import TokenType

class Token(object):

    type = TokenType
    text = ""
    pos = 0

    def __init__(self ,type ,text ,pos):
        self.type = type
        self.text = text
        self.pos = pos
