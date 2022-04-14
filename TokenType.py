TOKEN_TYPES = [('NUMBER', r'[0-9]\d'), ('IDENTIFIER', r'[A-Z]\d'), ('SEMICOLON', ';'),
               ('SPACE', r'[\\n\\n\\r]'), ('ASSIGN', '='), ('+', '+'), ('-', '-'), ('LPAR', '('), ('RPAR', ')')
               ]


class TokenType:
    name = ""
    regex = ""

    def __init__(self, name, regex):
        self.name = name
        self.regex = regex


TOKEN_TYPES_LIST = [('void', TokenType('TYPE', r'^void')), ('int', TokenType('TYPE', r'^int')),
                    ('return', TokenType('KEY_WORD', r'^return')), ('if', TokenType('if', r'^if')),
                    ('else_if', TokenType('else_if', r'^else if')), ('else', TokenType('else', r'^else')),
                    ('for', TokenType('for', r'^for')), ('NUMBER', TokenType('NUMBER', r'^[0-9]+')),
                    ('VARIBALE', TokenType('Identifier', r'^[A-Za-z_]+')),
                    ('SEMICOLON', TokenType('SEMICOLON', r'^;')), ('<', TokenType('<', r'^<')),
                    ('>', TokenType('>', r'^>')), ('==', TokenType('==', r'^==')), ('!=', TokenType('!=', r'^!=')),
                    ('SPACE', TokenType('SPACE', r'^\s|^\,')), ('ASSIGN', TokenType('ASSIGN', r'^=')),
                    ('+', TokenType('ADD', r'^\+')), ('-', TokenType('SUB', r'^\-')), ('*', TokenType('MULT', r'^\*')),
                    ('/', TokenType('DIV', r'^/')), ('LPAR', TokenType('LPAR', r'^\(')),
                    ('RPAR', TokenType('RPAR', r'^\)')), ('LSHAPE', TokenType('LShape', r'^\{')),
                    ('RSHAPE', TokenType('RShape', r'^\}'))
                    ]
