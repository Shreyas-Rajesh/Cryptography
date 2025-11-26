from math import gcd
# Fermats Little theorem
a = 273246787654
m = 65536
p = 65537

print(gcd(a,p)) # they aren co - prime, so its 1
print(pow(a,m,p))