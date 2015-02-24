__author__ = 'LICT_2'
basic = 100000
mb = 0
if basic * .25 >= 10000 and basic * .25 > 5000:
    mb = 200
elif basic * .25 <= 5000 and basic * .25 > 2000:
    mb = 100
elif basic * .25 <= 2000:
    mb = 0
print("MB:",mb)
