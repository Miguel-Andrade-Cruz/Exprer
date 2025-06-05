from handlers.priorityPicker import priorityPicker
from handlers.hasOperations import hasOperations
from core.calculator import calculate

def evaluation(exp: str) -> float:
    """"
    Evaluates entire expression
    """

    if hasOperations(exp) == 0:
        return float(exp)

    elif hasOperations(exp) == 1:
        return float(calculate(exp))
    
    elif hasOperations(exp) >= 2:
        priority_exp, priority_symbols = priorityPicker(exp)
        priority_result = calculate(priority_exp)

        return evaluation(exp.replace(
            priority_symbols['delimiter_open'] + priority_exp + priority_symbols['delimiter_close'],
            priority_result
            )
        )
    