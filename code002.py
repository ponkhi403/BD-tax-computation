__author__ = 'LICT_2'
basic=100000
medical_allowance=basic *.05
if basic>80000:
    bonus=basic *.02
else:
    bonus=0
print("basic:",basic)
print("medical_allowance:",medical_allowance)
print("bonus:",bonus)

