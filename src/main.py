from core.eval import evaluation

def main() -> None:
    exp:str = input("Enter the expression to evaluate: ")

    print(evaluation(exp))

if __name__ == "__main__":
    main()