def transpose(l):
  new_l=[]
  for i in range(len(l[0])):
    temp=[x[i] for x in l]
    new_l.append(temp)
  return new_l

print(transpose([[12,9]]))