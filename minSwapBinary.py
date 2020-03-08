import random

def main():

    maxArrays = input("Enter the number of arrays you want to generate: ")
    maxLength = input("Enter the maximum of length of an array: ")
    viewArr = input("Would you even like to view your Arrays? \n"
                    "Press 1 for yes and 2 for no.")

    start(int(maxArrays), int(maxLength), int(viewArr))





def start(mA, mL, vA):
    maxNoOfArrays = mA
    maxLenOfArray = mL

    arr = []
    for _ in range(maxNoOfArrays):
        arr.append([])
    for elem in arr:
        lenOfArray = random.randint(1,maxLenOfArray)
        for _ in range(lenOfArray):
            elem.append(random.randint(0,1))
        print("Size of array is :", lenOfArray)
        val = minSwap(elem)
        print("Minimum number of swaps required to group: ", val)
        if (vA == 1):
            print(elem)

def minSwap(arr):

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
    return(myans)


if __name__ == '__main__':
    main()
