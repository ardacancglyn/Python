#List Comprehension

#1-)
print("1-): ")
list1=[1,2,3,4,5,6,7,8,9,10]

list2=list()

for i in list1:
    list2.append(i)
print(*list2)

#2-)1. SAME(Basic)
print("2-): ")
    
list3=list(range(1,21))
liste = []

for i in range(1000):
    liste += [i]
#2-)2.SAME (Comprehension)
liste1 = [i for i in range(1000)]



#3-)1. SAME(Basic)
liste = []
for i in range(1000):
    if i % 2 == 0:
        liste += [i]
#3-)2. SAME(Comprehension)
liste = [i for i in range(1000) if i % 2 == 0]

        
        
        
        
        
        
        
        