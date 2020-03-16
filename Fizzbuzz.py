for i in range(1,51):
    if (i%15==0):
        print(i,'= FIZZBUZZ')
    elif i%5==0:
        print(i,'= Buzz')
    elif i%3==0:
        print(i,'= Fizz')
    else:
        print(i)
