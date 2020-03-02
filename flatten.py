def listtype(l):
  if (type(l) == type([])) or type(l)==type(()):
      return True
  else:
      return False

def flatten(l):
  new_l=[]
  for x in l:
    if listtype(x):
      new_l.extend(flatten(x))
    else:
      new_l.append(x)
  return new_l

print(flatten([1,2,[3],(4,[5,6])]))