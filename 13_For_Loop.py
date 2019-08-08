#For


#1-)Addition
print("1-): ")
list1=[1,2,3,4,5,6,7,8,9,10]

add=0
for i in list1:
    add+=i
print("{} ".format(add)+ "Addition.")


#2-)Odd and Even Number
print("2-): ")
for a in list1:
    if a %2==0:
        print("{} ".format(a) + "Even Number.")
    elif a % 2!=0:
        print("{} ".format(a) + "Odd Number.")

#3-)
print("3-): ")
list2=[(1,2),(3,4),(5,6)]
        
for x,y in list2:
    print("x: ")
    print(x)
    print("y: ")
    print(y)
    print("x,y: ")
    print(x,y)
        

#4-)
print("4-): ")
dic={"x":"1","y":"2","z":"3"}
print(dic.items())
print(dic.keys())
print("İtems: ")
for k,l in dic.items():
    print(k,l)

print("Keys: ")
for n in dic.keys():
    print(n)
    
    
    
    
    
    
