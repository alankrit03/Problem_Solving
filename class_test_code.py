class CSStudent:
    stream='cse'

    def __init__(self,roll):
        self.rollnum=roll

    def __repr__(self):
        return "From repr method Test a:%s " % (self.rollnum)

    def __str__(self):
        return "From str method of Test: a is %s," % (self.rollnum)


a=CSStudent(1033)
print(a.rollnum)
print(a.stream)
print([a])
print(a)