def calculate(exp: str) -> str:
    """"
    Caculates the expression
    """
    
    splitted_exp = exp.split(' ')
    if splitted_exp[1] == '+':
        return str(float(splitted_exp[0]) + float(splitted_exp[2]))
    
    elif splitted_exp[1] == '-':
        return str(float(splitted_exp[0]) - float(splitted_exp[2]))

    elif splitted_exp[1] == '*':
        return str(float(splitted_exp[0]) * float(splitted_exp[2]))
    
    elif splitted_exp[1] == '/':
        if float(splitted_exp[2]) == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return str(float(splitted_exp[0]) / float(splitted_exp[2]))
