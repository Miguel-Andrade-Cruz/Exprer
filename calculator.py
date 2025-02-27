def calculate(**only_exp):
    
    value_one = int(only_exp["value_one"])
    value_two = int(only_exp["value_two"])
    
    match only_exp["operator"]:
        case "+":
            return value_one + value_two
        case "-":
            return value_one - value_two
        case "*":
             return value_one * value_two
        case "/":
             return value_one / value_two
             
            
if __name__ == "__main__":
    print(calculate("3", "+", "3"))