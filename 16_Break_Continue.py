#Break
print("Break: ")
#1-)  we want  if x=5  loop finish
print("1-): ")
x=1
while(x<10):
    print(x)
    if x ==5:
        break
    x+=1

#2-)
print("2-): ")
for i in range(1,20):
    print(i)
    if i==8:
        break

#Continue
print("Continue: ")
#1-)
print("1-): ")
for x in range(1,50):
    if x % 3==0:
        continue
    print(x)

