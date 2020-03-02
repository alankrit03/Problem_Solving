def matrixflip(m,d):
    copy_m=[]
    if d=='h':
        for j in range(len(m)):
            temp=[]
            for i in range(len(m)):
                temp.append(m[j][-i-1])
            copy_m.append(temp)
    elif d=='v':
        copy_m.reverse()
    return copy_m