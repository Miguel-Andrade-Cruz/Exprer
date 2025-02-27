#Fazendo um calculador de expressões numéricas
from eval import eval
  
def main():
    
    expression = input('Insira sua expressão: ')
    
    if expression == False:
        
        print("Não existe expressão")
        return
        
    try:
        answer = eval(expression)
        print(f"O resultado da expressão é: {answer}")
        return
    except:
        print("Expressão inválida ou erro interno")
        return
    
if __name__ == "__main__":
    main()