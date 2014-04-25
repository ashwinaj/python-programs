# Find intersection and union of arrays using while loop

def intersection(arr1, arr2):
    s = []
    i = 0 
    j = 0
    
    print "Intersection is: "
    
    while i < len(arr1):
        if arr1[i] == arr2[j]:
            s.append(arr1[i])
            print arr1[i]
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1

    #print "Intersection is: ", s
    

def union(arr1, arr2):
    s = []
    i = 0
    j = 0
    
    print "Union is: "
    while i < len(arr1):
        if arr1[i] < arr2[j]:# and arr1[i] not in s:
            s.append(arr1[i])
            print arr1[i]
            i+=1
        elif arr1[i] > arr2[j]:# and arr2[j] not in s:
            s.append(arr2[j])
            print arr2[j]
            j+=1
        else:
            s.append(arr1[i])            
            print arr1[i]
            i+=1
            j+=1
           
   
    if len(arr1) > len(arr2):
        while i < len(arr1):
              s.append(arr1[i])
              print arr1[i]
              i+=1
    else:
        while j < len(arr2):
              s.append(arr2[j])
              print arr2[j]
              j+=1

    #print "Union is: ", s
    
 
if __name__ == "__main__":
    arr1 = [1,4,5,8,9,12]
    arr2 = [1,3,7,8,12,13,15,45,67,78]

    intersection(arr1, arr2)
    union(arr1, arr2)
