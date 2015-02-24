__author__ = 'LICT_2'
year_gross = 1000000
year_gross2 = year_gross - 220000
#print(year_gross2)

if year_gross <= 220000:
    print("hello")
    tax = 0
elif year_gross2 <=300000 and year_gross2 >= 220001:
    print("hello")
    tax_two = year_gross2 * .10
    print (tax_two)

