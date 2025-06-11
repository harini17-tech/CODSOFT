def add(x, y):
    return x + y
def subract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return "Error: Division by zero"
    return x / y

def main():
    print("Simple Calculator")
    print("Select Operation: ")
    print("1.Add ")
    print("2.Subract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter the choice (1/2/3/4): ")
    if choice not in ['1','2','3','4']:
        print("Invalid Input")
        return
    try:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
    except ValueError:
        print("Invalid Number Input")
        return
    if choice=='1':
        print("Result is ",add(n1,n2))
    elif choice=='2':
        print("Result is ",subract(n1,n2))
    elif choice=='3':
        print("Result is ",multiply(n1,n2))
    elif choice=='4':
        print("Result is ",divide(n1,n2))
if __name__=="__main__":
    main()
