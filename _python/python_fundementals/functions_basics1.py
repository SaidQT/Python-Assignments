def countdown(n):
    target = []
    for i in range(n, -1, -1):
        target.append(i)
    return target

def print_return(x):
    print (x[0])
    return x[1]


def sum(list):
    return list[0]+len(list)


def greaterThanSecond(list):
    new_list=[]
    if len(list)<2:
        return False
    for i in range(0,len(list),1):
        if list[i]>list[1]:
            new_list.append(list[i])

    
    print(len(new_list))
    return new_list


def size_and_value(size,value):
    newList=[]

    for i in range(size):
        newList.append(value)
    return newList
    
print(size_and_value(4,2))