def eulcidian(a,b):
    if b == 0:
        return a
    return eulcidian(b,a%b)

a = 66528
b = 52920

print(eulcidian(a,b))