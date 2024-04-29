import random
def randInt(min= None, max=None):
    num = random.random()
    if min==None and max == None:
        num=round(num*100)
    elif min==None and max!=None:
        num=round(num*max)
    elif min!=None and max==None:
        num=round(num*(100-min)+min)
    elif min!=None and max!=None:
        num=round(num*(max-min)+min)
    return num



