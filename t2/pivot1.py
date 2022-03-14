list_1=[1,8,12,9,1,5,12,21,3,4,9,2,5]
tf=[]
for i in range(1,len(list_1)):
    if i==0:
        pass
    elif list_1[i-1] > list_1[i]:
        tf.append(1)
    else:
        tf.append(2)
count=[]
print(tf)
for i in range(1,len(tf)):
    if tf[i] != tf[i-1]:
        count.append(i)
print(count)

