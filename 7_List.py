#List

#1-
print("1-: ")
list_1=[5,9,7,1,2,3,"user"]
print(*list_1)
print(type(list_1))
print(len(list_1))

#2-List İndex
print("2-: ")
print(list_1[0])
list_1[0]=100000
print(list_1[0])

#3-String to List 
print("3-: ")
x="the best user"
list_x=list(x)
print(list_x)

#4-List to String
print("4-: ")
X=""
y=["abc","def"]
for i in y:
    X+=i
print(X)    


#5-  Append Values to List
print("5-: ")
list_3=[1,2,3,4,5,6,7,8,9,10]
list_3_1=list_3 * 3
print(list_3_1)
list_3=list_3 + [11]
list_3=list_3 +["hello"]
print(list_3)
#5.1
list_3.append(999)
print(list_3)
apx=1000000
list_3.append(apx)
print(list_3)


#6-Ranking
print("6-: ")
list_4=[9,7,4,5,6,1,4,5,8,10,90,75,62]
list_4.sort()
print(list_4)

#7-Alphabetical Ranking
list_5=["john","cassidy","sussexy","zen"]
list_5.sort()
print(list_5)







