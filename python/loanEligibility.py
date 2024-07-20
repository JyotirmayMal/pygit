#check if a person is eligible for loan or not
min_income=2000
age = int(input("Enter your age : "))
income = float(input("Your salary in $ : "))
has_loans = bool(input("false if NO and true if YES ").lower())
print(has_loans)
if (age>=18) and (income >=min_income) and (has_loans==False):
    print("You are eligible for loan")
else:
    print("You are not eligible for loan")