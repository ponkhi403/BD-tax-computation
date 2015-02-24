__author__ = 'Tanzil Khan'
Gross_Salary = int(input("Enter your Total Salary:"))
if(Gross_Salary <= 220000):
    Tax = 0
elif((Gross_Salary <=520000 and Gross_Salary > 220000)and (Gross_Salary <=920000 and Gross_Salary > 520000)):
    Tax1 = ((Gross_Salary-220000)*.15) and ((Gross_Salary-520000)*.20)
    Total_Tax = (Tax+Tax1)
    print (Total_Tax)
print("Hello")