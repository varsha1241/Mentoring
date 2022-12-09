from numpy import ndarray
print("Enter the number of coefficients")
coefficient=int(input())
array= ndarray((coefficient*2,),int)
j=0
k=0
# print(len(array))
for i in range (len(array)):
    array[i]=int(input())
# print(array)
coefficient_array= ndarray((coefficient,),int)
exponent_array= ndarray((coefficient,),int)
for i in array[1::2]:
    exponent_array[j]=i
    j=j+1
for i in array[0::2]:
    coefficient_array[k]=i
    k=k+1
print(coefficient_array)
print(exponent_array)
maximum=(max(exponent_array))

tuple1=()
max = maximum
# print(maximum)
for i in range(maximum):
    # print(i)
    for j in range (coefficient):
        if(max==exponent_array[j]):
            tuple1 += (coefficient_array[j],)
            max-=1
            print(max)
    # j=coefficient
    # if(maximum==exponent_array[j]):
    #     tuple1+=(coefficient_array[i],)
    #     maximum=maximum-1
    # else:
    #     tuple1+=(0,)
    #     maximum=maximum-1
print(tuple1)

