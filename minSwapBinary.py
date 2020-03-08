def main():

    # print("Hello World!")
    # arr = [1,0,0,1,1,0,0,1,1,0,0,1]
    # arr = [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1]
    # arr = [1,0,0,0,0,0,0,0,0,1,1]
    # arr = [1,0,0,0,0,0,1]
    # arr = [1,0,1,0,0,0,0,0,0,1]

    arr = [1,0,1]
    size = len(arr)
    noOfzeroes = 0
    minswaps = 0

    # count no of zeros
    # when see a 1, add no of zeros to ans and set no of zeros to zero
    # whenever see 1, check no of, if zero, add ans to ans. else add ans plus no of zeros

    one = arr[0]
    for i in range(0, size):
        if(arr[i] == one):
            if(noOfzeroes == 0):
                minswaps = minswaps+minswaps
            else:
                minswaps = minswaps +noOfzeroes
                noOfzeroes = 0
        else:
            noOfzeroes = noOfzeroes+1



    # Gotta check in reverse too
    minswapsRev = 0
    noOfzeroesRev = 0
    one = arr[size-1]
    for i in range(size-1, -1, -1):
        if(arr[i] == one):
            if(noOfzeroesRev == 0):
                minswapsRev = minswapsRev + minswapsRev
            else:
                minswapsRev = minswapsRev + noOfzeroesRev
                noOfzeroesRev = 0
        else:
            noOfzeroesRev = noOfzeroesRev +1

    myans = min(minswapsRev, minswaps)
    print(myans)

if __name__ == '__main__':
    main()
