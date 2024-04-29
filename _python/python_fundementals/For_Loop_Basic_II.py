
def biggieList(list):
    new_list=[]
    for i in range (len(list)):
        if list[i]>0:
            list [i]="big"
        new_list.append(list[i])
    return new_list

def positiveNumber(x):
    count=0
    for i in range (len(x)):
        if x[i]>0:
            count +=1
    x[len(x)-1]=count
    return x

def sumList(y):
    count=0
    for i in range(len(y)):
        count+=y[i]
    return count

def avgList(y):
    count=0
    sum=0
    for i in range (len(y)):
        count+=1
        sum+=y[i]
    avg=sum/count
    return avg

def lengthList(x):
    return len(x)

def minValue(x):
    if len(x)==0:
        return False
    return min(x)

def maxValue(x):
    if len(x)==0:
        return False
    return max(x)

def dictList(list):
    newDict={}
    newDict['sumTotal']=sumList(list)
    newDict['average']=avgList(list)
    newDict['minimum']=minValue(list)
    newDict['maximum']=maxValue(list)
    newDict['length']=lengthList(list)
    return newDict

def reverseList(list):
    list[:]=list[::-1]
    return list



