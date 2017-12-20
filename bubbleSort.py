# bubble sort
def bubbleSort(a):
    length = len(a)
    if length < 2:
        return a
    for i in range(length):
        for j in range(length-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def main():
    a = [1,12,3,2,43,5,]
    bubbleSort(a)
    print(a)

main()