arr=[20,2,14,30,40,50,60,70,80,90,100]
def maximum(arr):
    max=arr[0]
    #print('Number is '+str(max))
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
    
max=maximum(arr) 
print(max)