print("*Select a operater*")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input for operation
oprt =float(input("Enter Operater 1/2: "))
# Check for valid operation
if oprt not in [1,2,3,4]:
    print("!Invaild operater!")
 # Get user input for numbers
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))

  # Perform calculation
if oprt == 1:
    total = num1+num2
    print("Total: ",total)
elif oprt == 2:
    total = num1-num2
    print("Total: ",total)
elif oprt == 3:
    total = num2*num2
    print("Total: ",total)
else :
    total = num1/num2
    print("Total: ",total)
