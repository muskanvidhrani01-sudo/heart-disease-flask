Gender=input("Enter Gender ")
Name=input("Enter Name ")

if Gender=="Male":
    print(f"Mr. {Name}")
elif Gender=="Female":
    Marital_Status=int(input("What is your Marital Status: 1.Married 2.Unmarried "))
    if Marital_Status==1:
        print(f"Ms. {Name}")
    elif Marital_Status==2:
        print(f"Miss. {Name}")
