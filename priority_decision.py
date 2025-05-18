def priorityPicker(exp: str) -> str:
    """"
    Decides what evaluation should be done first
    """

    if exp.find('(') != -1:
        open = exp.find('(')
        close = exp.find(')')
        return exp[open+1:close], ['(', ')']
    
    elif exp.find('[') != -1:
        open = exp.find('[')
        close = exp.find(']')
        return exp[open+1:close], ['[', ']']

    elif exp.find('{') != -1:
        open = exp.find('{')
        close = exp.find('}')
        return exp[open+1:close], ['{', '}']
    
    else: 
        spliited_exp = exp.split(' ')
        return spliited_exp[0] + " " + spliited_exp[1] + " " + spliited_exp[2], ['', '']


if __name__ == "__main__":
    exp = "2343423 + 234324 / 12 + 1"
    print(priorityPicker(exp))