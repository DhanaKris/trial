# mytuple=("Dk",) # if comma is not written then it is string
# print(type(mytuple))
# print(mytuple.index("Dk"))

mytuple=('d','h','a','n','a','k','r','i','s','h')
# lst=[mytuple]
# print(type(lst))

t1, *t2, t3=mytuple
print(t1)
print(t2)
print(t3)

#tuple and list:
# tuple is more efficient when working with lare data.
#list more size less time to create

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))


