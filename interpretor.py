from variables.Var import Var
tokenList = {
    "int": int,
    "str": str,
    '"': "sep",
    "'": 'sep',
    'printf': 'keyword',
    'var': 'keyword',
    '(': 'sep',
    ')': 'sep',
}

def interpret(tokens):
    definesVar = False
    varId = ''
    varVal = ''
    varInfo = 0
    for key in tokens:
        val = tokens[key]
        if key == 'keyword' and val == 'var': definesVar = True
        elif key == 'id' and definesVar:
            varId = val
            varInfo += 1
        elif key == 'val' and definesVar:
            varVal = val
            varInfo += 1
            if varInfo == 2:
                varId = Var(varId, varVal)

interpret(tokens={'keyword': 'var', 'id': 'hello', 'op': '=', 'val': '"Hello'})
