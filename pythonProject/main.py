list1=[2,2,6,5,3,3]
def unique_list(input_list):
    tmp_list=[]
    for i in input_list:
        if i not in tmp_list:
            tmp_list.append(i)
    return tmp_list
test=[1,2,2,5,1,8,5]
print(unique_list(test))