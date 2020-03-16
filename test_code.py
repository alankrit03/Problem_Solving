import itertools
#print(list(itertools.filterfalse(lambda x: x%2 , range(15))))

from collections import namedtuple
a='Price'
b='Mileage'
c='Colour'
d='Class'
lst=[a,c,b,d]
Cars = namedtuple('Sedan',lst   )
xyz = Cars(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print (xyz)

print (xyz.Class)
