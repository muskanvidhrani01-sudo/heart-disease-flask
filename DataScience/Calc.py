num1=float(input("Enter number1 "))
num2=float(input("Enter number2 "))
operator=input("Enter Operator ")

if operator=="+":
    res=num1+num2
elif operator=="-":
    res=num1-num2
elif operator=="*":
    res=num1*num2
elif operator=="/":
    res=num1/num2

print(round(res,3))
