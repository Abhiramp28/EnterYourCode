def add(a,b):
    return a+b
def dif(a,b):
    return a-b
def pro(a,b):
    return a*b
def div(a,b):
    return a/b
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter your choice: ")
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(add(a,b))
            break

        elif choice == '2':
            print(dif(a,b))
            break

        elif choice == '3':
            print(pro(a,b))
            break

        elif choice == '4':
            print(div(a,b))
            break 
        
    else:
        print("Invalid Input")
