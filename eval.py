from priority_decision import priorityPicker
from handler import hasOperations
from calculator import calculate

def evaluation(exp: str) -> float:
    """"
    Evaluates entire expression
    """

    if hasOperations(exp) == 0:
        return float(exp)

    elif hasOperations(exp) == 1:
        return float(calculate(exp))
    
    elif hasOperations(exp) >= 2:
        priority_exp, priority_sympbols = priorityPicker(exp)
        priority_result = calculate(priority_exp)
        

        return evaluation(exp.replace(
            priority_sympbols[0] + priority_exp + priority_sympbols[1],
            priority_result
            )
        )
    else:
        raise ValueError("Invalid expression")