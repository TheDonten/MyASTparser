from Tokens import  Token
from TokenType import TokenType, TOKEN_TYPES_LIST
import re


class lexer:
    code = ""
    pos = 0
    tokenList = []

    def __init__(self,code):
        self.code = code


    def lexAnalysis(self):
        while (self.nextToken()):
            continue
        return self.tokenList

    def nextToken(self):
        if self.pos >= len(self.code):
            return False
        tokenTypesValues = TOKEN_TYPES_LIST
        for i in tokenTypesValues:
            tokenType = i[1].name
            regex  =    i[1].regex
            # result = self.code[self.pos:].find(regex)
            str = self.code[self.pos:]
            result = re.search(regex,str)
            if result is None:
                continue

            result = result.group(0)
            token = Token(tokenType,result,self.pos)
            if token.type == 'SPACE':
                self.pos += len(result)
                return True
            self.pos += len(result)
            self.tokenList.append(token)
           # print(result)
            return True

        raise ValueError('Na pozicii',self.pos , 'obnaruzena oshibka')