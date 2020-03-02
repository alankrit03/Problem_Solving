def rainaverage(l):
    rain_dict = {}
    for x, y in l:
        if x in rain_dict:
            rain_dict[x].append(y)
        else:
            rain_dict[x] = [y]
    for x in rain_dict.keys():
        rain_dict[x]=sum(rain_dict[x]) / len(rain_dict[x])
    l = [(x, y) for x, y in rain_dict.items()]
    print(l)

rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])