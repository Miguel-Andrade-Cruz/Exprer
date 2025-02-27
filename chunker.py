def chunkOperations(splitted_exp):
    operators = [ sym for sym in splitted_exp if sym in ["+", "-", "*", "/"] ]
    chunks = []
    for operator in operators:
        operator_pos = splitted_exp.index(operator)
        
        value_one = splitted_exp[operator_pos - 1]
        value_two = splitted_exp[operator_pos + 1]
        
        chunk = [ value_one, operator, value_two ]
        
        chunks.append(chunk)
        splitted_exp.remove(operator)
    return chunks
        
        
if __name__ == "__main__" :
    print(chunkOperations(["3", "+", "3", "+", "3", "+", "3"]))