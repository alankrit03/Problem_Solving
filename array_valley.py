
def valley(l):
  status = "negative"
  count_des,count_asc=1,1
  des_status,asc_status="start",''
  for i in range(len(l)-1):
    if l[i]-l[i+1]==0:
      return False
    elif l[i]-l[i+1]>0:
      if asc_status=='start':
        return False
      else:
        count_des+=1
    else:
      asc_status='start'
      count_asc+=1
  print(count_des,count_asc)
  return True

if __name__=='__main__':
    lst=list(map(int,input().split()))
    print(valley(lst))4