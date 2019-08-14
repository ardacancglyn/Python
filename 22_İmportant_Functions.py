                                #Functions

#1-) map()
print("1-)<<<MAP>>>")
#Not map
print("Classic (Not Map() ): ")
def x(list1):
    list2=list()
    for i in list1:
        list2.append(i**2)
    return list2
print(x([1,2,3,4,5,6,7,8,9,10]))


#This is map()
print("Map(): ")
def y(lists):
    return lists**2
print(list(map(y,[1,2,3,4,5,6,7,8,9,10,11])))

#Map() and Lambda
print("Map and Lambda: ")
a=list(map(lambda x : x**2,[1,2,3,4,5,6]))
print(a)



#2-)reduce()
print("2-)<<<Reduce>>>")

from functools import reduce

a=reduce(lambda x,y :x+y,[1,2,3,4,5])
print(a)

#Algorithm>>>  x=1,y=2   x+y=3 now  x=3,y=3 x+y=6   now x=6,y=4  x+y=10 now x =10,y=5 x+y =15 





#3-) max-min ()
print("<<<Max-Min>>> ")
l1=[1,2,3,7,9,590]
print("Min: ")
print(min(l1))
print("Max: ")
print(max(l1))


#4-) zip()
print("<<<Zip>>>")

x1=[1,2,3,4,5]
y1=["a","b","c","d","e"]

print(list(zip(x1,y1)))


#5-)enumerate()
print("<<<Enumerate>>>")
enum=list(enumerate(["a","b","c"]))
print(enum)
# 0. index = a  1.index=b  2.index=c

#6-) filter()
print("<<<Filter>>>")
filt=list(filter(lambda x: x%2==0,[x for x in range(101)]))
print(filt)


#7-)all and any ()
print("<<<All>>>")

#not all
def turnvalues(x):
    for i in x:
        if not i:
            return False
    return True
listx=[True,True,True]
listy=[False,True,True]
print("Listx: ")
print(turnvalues(listx))
print("Listy: ")
print(turnvalues(listy))

#all()
print("All(): ")
listz=[True,False]
listq=[True,True]
print("Listz: ")
print(all(listz))
print("Listq: ")
print(all(listq))



#any()
print("Any(): ")
listz=[True,False]
listq=[True,True]
listk=[False,False]
print("Listz: ")
print(any(listz))
print("Listq: ")
print(any(listq))
print("Listk: ")
print(any(listk))












