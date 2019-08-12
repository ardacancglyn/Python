#Functions
list1=[1,2,3,4,5,2,6,2]

#1-)
print("Append Number or Str Values: ")
list1.append(7)
print(list1)

#2-)
print("Type: ")
print(type(list1))

#3-)
print("How Many Numbers On The List: ")
x=list1.count(2)
print(x)

#4-)
print("Reverse: ")
list2=[10,20,30,40,50,60]
list2.reverse()
print(list2)

#5-)DEF V1 :)
print("Def-1: ")
def addition(a,b):
    return a+b
defadd=addition(5,9)
print(defadd)
print(type(addition))

#6-)DEF V2 :)
print("DEF-2: ")
def add(k,l):
    print(k+l)
add(1,4)

#7-)DEF V3 :)
print("DEF-3: ")
def information(name,age,gender):
    print("""
          Name:%s
          Age:%s
          Gender:%s
          """ %(name,age,gender))

information("Joshua","30","Male")

#DEF V4 :)
print("DEF-4: ")
Name=None
Age=None
Gender=None

Name=input("Write Your Name: ")
Age=int(input("Write Your Age: "))
Gender=input("Write Your Gender: ")
print("""
        Name:%s
        Age:%s
        Gender:%s
        """ %(Name,Age,Gender))


#DEF V5 :) (Addition)
print("DEF-5(Addition With Def): ")
def function(*args):
    additions=0
    for i in args:
        additions += i
    return additions
print(function(1,2,3,4,5,6,7,8,9,10))













