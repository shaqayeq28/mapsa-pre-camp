num=int(input())
num_list=list(input())
for k in range(len(num_list)):
    num_list[k]=int(num_list[k])
num_list2=num_list.copy()
counter=0

for i in range(1,len(num_list)-1):
    if num_list[i]>num_list[i-1] and num_list[i]> num_list[i+1] :
        if num_list[i-1]!=num_list2[i-1]:
            num_list[i-1]=num_list[i]
        else:
            num_list[i+1]=num_list[i]
for i in range(len(num_list2)):
    if num_list[i] != num_list2[i]:
        counter+=1


print(counter)
print(num_list)