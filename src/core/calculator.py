def calculate(exp: str) -> str:
    """"
    Caculates the expression
    """
    
    (operand_one, operator, operand_two) = exp.split(' ')
    if operator == '+':
        return str(float(operand_one) + float(operand_two))
    
    elif operator == '-':
        return str(float(operand_one) - float(operand_two))

    elif operator == '*':
        return str(float(operand_one) * float(operand_two))
    
    elif operator == '/':
        if float(operator) == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return str(float(operand_one) / float(operand_two))
    
    elif operator == '**': 
        return str(float(operand_one) ** float(operand_two))
