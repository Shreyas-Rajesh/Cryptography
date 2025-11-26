# Find x and y for:
# 11 congruent x (mod 6)
# 8146798528947 congruent y (mod 17)

from math import gcd
#checking if they are co-prime
print(gcd(11,6))
print(gcd(8146798528947,17)) 

#since they are coprime x congurnet to 11 * invers_1 (mod 6)
x = (11 * pow(1,-1)) % 6
y = (8146798528947 * pow(1,-1)) % 17

print(x,y)
