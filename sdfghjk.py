#bubblesort
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [-10, 47, 8, 32, 89, 23, 120]
#print("Given array:", a)

bubbleSort(a)
print("Sorted array:", a)


#hiring
def hiring(a):
    best = count = 0

    for i, rank in enumerate(a):
        if rank > best:
            best = rank
            count += 1
            print("Candidate", i+1, "hired")
        else:
            print("Candidate", i+1, "rejected")

    print("Highest rank:", best)
    print("Hiring operations:", count)

n = int(input("Enter number of candidates: "))
a = [int(input("Enter rank: ")) for _ in range(n)]
hiring(a)

def quicksort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1]
    left = [x for x in a[:-1] if x <= pivot]
    right = [x for x in a[:-1] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


a = list(map(int, input("Enter numbers: ").split()))
print("Sorted array:", quicksort(a))



def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[len(arr) // 2]
    
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]   
    right = [x for x in arr if x > pivot]   
    
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    community_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original Community:", community_list)
    
    sorted_community = quick_sort(community_list)
    print("Sorted Community:", sorted_community)
