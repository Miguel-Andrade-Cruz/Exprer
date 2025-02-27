from reader import partitionate
from chunker import chunkOperations
from calculator import calculate
from newExpression import backToExpression


def eval(exp):
    partitions = partitionate(exp)
    chunks = chunkOperations(partitions)
    
    if len(chunks) == 1 :

        if chunks[0][1] in ["*", "/"]:

            value_one = chunks[0][0]
            operator = chunks[0][1]
            value_two = chunks[0][2]
            
            equals_to = calculate(
                value_one=value_one,
                operator=operator,
                value_two=value_two
            )
            return equals_to
   
    if len(chunks) >= 2 :

        if chunks[0][1] in ["*", "/"]:
            value_one = chunks[0][0]
            operator = chunks[0][1]
            value_two = chunks[0][2]
            
            equals_to = calculate(
                value_one=value_one,
                operator=operator,
                value_two=value_two
            )

            new_exp = backToExpression(exp, chunks[0], equals_to)


            return eval(new_exp)

        value_one = chunks[0][0]
        operator = chunks[0][1]
        value_two = chunks[0][2]
        
        equals_to = calculate(
            value_one=value_one,
            operator=operator,
            value_two=value_two
        )

        new_exp = backToExpression(exp, chunks[0], equals_to)


        return eval(new_exp)

    
if __name__ == "__main__" :
    print(eval("3 + 12 - 3"))
