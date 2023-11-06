list1 = [1,2,8,7,6,9,3]
list2 = [3,5,8,7,4,15]

def common(a,b):
    common = []
    for i in range(len(list1)):
        if list1[i] in list2:
            common.append(list1[i])
    return common

commonString = common(list1,list2)
print(commonString)