def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operator_dict = {
               '+':add,
               '-':sub,
               '*':mul,
               '/':div
               }
def calculator():
    first_num=int(input("Enter the first number: "))
    calculation_flag=True
    while calculation_flag:
        for i in operator_dict:
                print(i)
        operator=input("pick an operator: ")
        second_num=int(input("Enter the second number: "))
        calculation=operator_dict[operator]
        output=calculation(first_num,second_num)
        print(f"{first_num} {operator} {second_num}= {output}")
        proceed=input(f"Enter 'x' to proceed calculation with the {output} or enter 'y' to start new calculation or 'z' to exit calculation: ").lower()
        if proceed=="x":
            first_num=output
        elif proceed=='y':
            calculation_flag=False
            calculator()
        else:
            calculation_flag = False
            print("Exit")
calculator()



