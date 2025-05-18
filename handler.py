def hasOperations(exp: str) -> int:
    """"
    Checks for quantity of operations
    """
    operations_quantity = 0
    for char in exp:
        if char in "+-*/": 
            operations_quantity += 1
    return operations_quantity



if __name__ == "__main__":
    exp = "(2343423 + 2343243) / 12"
    print(hasOperations(exp))
