__author__ = 'Tanzil Khan'

yg = 10000000
year_gross = yg - 220000

year_gross_slab2 = year_gross - 300000
if year_gross_slab2 < 0:
    year_gross_slab2 = 0

year_gross_slab3 = year_gross_slab2 - 400000
if year_gross_slab3 < 0:
    year_gross_slab3 = 0

year_gross_slab4 = year_gross_slab3 - 500000
if year_gross_slab4 < 0:
    year_gross_slab4 = 0

year_gross_slab5 = year_gross_slab4 - 3000000
if year_gross_slab5 < 0:
    year_gross_slab5 = 0

if yg <= 220000:
    taxzero = 0

if year_gross > 300000:
    tax = 300000*.10
elif year_gross < 300000:
    tax = year_gross * .10
print ("3lac level Tax:", tax)

if year_gross_slab2 > 400000:
    taxTwo = 400000 * .15
elif year_gross_slab2 < 400000:
    taxTwo = year_gross_slab2 * .15
print ("4lac level Tax:", taxTwo)

if year_gross_slab3 > 3000000:
    taxThree = 3000000 * .20
elif year_gross_slab3 < 3000000:
    taxThree = year_gross_slab3 * .20
print ("5lac level Tax:", taxThree)

if year_gross_slab4 > 3000000:
    taxFour = 3000000 * .25
elif year_gross_slab4 < 3000000:
    taxFour = year_gross_slab4 * .25
print ("30lac level Tax:", taxFour)

if year_gross_slab5 > 3000000:
    taxFive = year_gross_slab5 * .30
print ("3lac above level Tax:", taxFive)

nettax = tax + taxTwo + taxThree + taxFour + taxFive
print("Total Tax:", nettax)