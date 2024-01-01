from common_factor import *

a = factorisation(18)
b = 11
for i in a:
    i1 = i[0] + i[1]
    if i1 == b:
        print(i1, i)
        break
    i2 = -1*i[0] + i[1]
    if i2 == b:
        print(i2, i)
        break
    i3 = i[0] + -1*i[1]
    if i3 == b:
        print(i3, i)
        break
    i4 = -1*i[0] + -1*i[1]
    if i4 == b:
        print(i4, i)
        break