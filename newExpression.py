def backToExpression(old_expression, old_chunk, value_find):
    old_chunk = " ".join(old_chunk)
    new_expression = old_expression.replace(old_chunk, str(value_find))
        
    return new_expression
    
    
    
    
if __name__ == "__main__" :
   print(backToExpression("3", "1 + 2 + 3"))