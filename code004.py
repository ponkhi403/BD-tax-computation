__author__ = 'LICT_2'

print("Plz Enter your Basic Salary :")
basic = int(input())

print("Plz Enter your Child :")
child = int(input())


house_rent = basic * .60
conv = basic * .10
pf = basic * .10
medical = 5000
factory = basic *.10
gross = basic + house_rent + conv - pf + medical+factory
#print (gross)
#tax computation
if gross * 12 <= 240000:
    tax = 0
elif gross * 12 >= 240001:
    tax = 3000

#child allowance computation
child_allowance = 0
if child == 1:
    child_allowance = 2000
elif child >= 2:
    child_allowance = 4000

net_salary = basic + house_rent + conv - pf + medical - tax + child_allowance+factory

print("Tax :",tax)
print ("Net Salary :",net_salary)
print ("Child Allowance :",child_allowance)
