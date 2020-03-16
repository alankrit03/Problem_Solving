from collections import Counter

def majority(arr):

    # convert array into dictionary
    freqDict = Counter(arr)
    arr_list=list(dict(freqDict).items())
    arr_list.sort(key=lambda x:x[1],reverse=True)

    print(arr_list)
    if arr_list[0][1]>=(len(arr)//2):
        print(arr_list[0][0])


if __name__ == "__main__":
    arr = [3,3,4,2,4,4,2,4,4]
    majority(arr)