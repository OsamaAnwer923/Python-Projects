logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def dvd(n1,n2):
    return n1 / n2
operation = {"+":add, "-":sub, "*":mult, "/":dvd}


first_number = int(input("type the first number: "))
repeat = True
while repeat == True:
    operations_symbol = input("+\n-\n*\n/\nPick an operator: ")
    second_number = int(input("type the second number: "))
    result = operation[operations_symbol](first_number,second_number)
    print(f'{first_number} {operations_symbol} {second_number} = {result}')
    repeatation = input("if you want to continue with this calculation type 'yes' and "
                        "if you want to start new calculation type 'no' ").lower()
    if repeatation == 'yes':
        first_number = result
        repeat = True
    else:
        first_number = int(input("type the first number: "))
        