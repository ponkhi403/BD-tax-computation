__author__ = 'LICT_2'
child = int(input())
child_allowance = 0
if child == 1:
    child_allowance = 2000
elif child >= 2:
    child_allowance = 4000
print (child_allowance)

if 220000 >= gross * 12:
    taxable_amount1 = gross - 220000
print(taxable_amount1)
tax1 = taxable_amount1 * 0

if 300000 >= taxable_amount1 and taxable_amount1 >= 220001:
    taxable_amount2 = taxable_amount1 - 220000
tax2 = taxable_amount2 * .10
print (tax2)