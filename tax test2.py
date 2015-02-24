__author__ = 'Tanzil Khan'

month = float(input("Enter Your Monthly Salary Amount: "))

#Calculate Yearly Gross Salary
yg = month*12

#Second Slab Taxable Amount Computer from Gross Salary (221k - 300k)
year_gross = yg - 220000
if year_gross < 0:
    year_gross = 0

#Third Slab Taxable Amount Computer from Gross Salary (301k - 400k)
year_gross_slab2 = year_gross - 300000
if year_gross_slab2 < 0:
    year_gross_slab2 = 0

#Fourth Slab Taxable Amount Computer from Gross Salary (401k - 500k)
year_gross_slab3 = year_gross_slab2 - 400000
if year_gross_slab3 < 0:
    year_gross_slab3 = 0

#Fifth Slab Taxable Amount Computer from Gross Salary (501k - 3000k)
year_gross_slab4 = year_gross_slab3 - 500000
if year_gross_slab4 < 0:
    year_gross_slab4 = 0

#Sixth Slab Taxable Amount Computer from Gross Salary (3000k above)
year_gross_slab5 = year_gross_slab4 - 3000000
if year_gross_slab5 < 0:
    year_gross_slab5 = 0

#Tax at First Level
if yg <= 220000:
    taxzero = 0

#Tax at Second Level
if year_gross > 300000:
    tax = 300000*.10
elif year_gross < 300000:
    tax = year_gross * .10
print ("3lac level Tax:", tax)

#Tax at Third Level
if year_gross_slab2 > 400000:
    taxTwo = 400000 * .15
elif year_gross_slab2 < 400000:
    taxTwo = year_gross_slab2 * .15
print ("4lac level Tax:", taxTwo)

#Tax at Fourth Level
if year_gross_slab3 > 3000000:
    taxThree = 3000000 * .20
elif year_gross_slab3 < 3000000:
    taxThree = year_gross_slab3 * .20
print ("5lac level Tax:", taxThree)

#Tax at Fifth Level
if year_gross_slab4 > 3000000:
    taxFour = 3000000 * .25
elif year_gross_slab4 < 3000000:
    taxFour = year_gross_slab4 * .25
print ("30lac level Tax:", taxFour)

#Tax at Sixth Level
if year_gross_slab5 == 3000001:
    taxFive = 3000001 * .30
elif year_gross_slab4 > 3000001:
    taxFive = year_gross_slab5 * .30
print ("30lac above level Tax:", taxFive)


nettax = tax + taxTwo + taxThree + taxFour + taxFive
print("Total Tax:", nettax)