num=map(int,input())
num=list(num)
print(num)
sum=[]
num2=num.copy()
for i in range(0,len(num2)-1):
    tmp = (num[i]+num[i+1])
    num[i]=tmp
    num.pop(i+1)
    sum.append(num)

print(sum)









