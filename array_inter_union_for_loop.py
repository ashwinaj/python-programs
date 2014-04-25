# Find intersection and union of arrays

def intersection(arr1, arr2):
    s = []
    for i in arr1:
        if i in arr2:
            s.append(i)

    print "Intersection is: ", s
    

def union(arr1, arr2):
    s = []
    for i, j in zip(arr1, arr2):
        if i < j and i not in arr2 and j not in arr1:
            s.append(i)
            s.append(j)
        elif i > j and i not in arr2 and j not in arr1:
            s.append(j)
            s.append(i)
        else:
            s.append(i)

    if len(arr1) > len(arr2):
        for i in arr1:
            if i not in s:
                s.append(i)
    else:
        for i in arr2:
            if i not in s:
                s.append(i)

    print "Union is: ", s
    
 
if __name__ == "__main__":
    arr1 = [1,4,5,8,9,12]
    arr2 = [1,3,7,8,12,13,15,45,67,78]

    intersection(arr1, arr2)
    union(arr1, arr2)
    
