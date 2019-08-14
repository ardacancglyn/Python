#Clusters

cl1={0,1,2,3,4,5,6,7,8,9}
cl2={0,5,9,10,50,97,45,84}

cl1.add(100)
print(cl1)

print(cl1.difference(cl2))
print(cl2.difference(cl1))


print("Discrete Cluster True or False: ")
print(cl1.isdisjoint(cl2))




cl3={1,2,3,4}
cl4={9,8,10,15}

print("Discrete Cluster True or False: ")
print(cl3.isdisjoint(cl4))




cl5={10,20,30,40}
cl6={10,20,40}
print("Subset True or False: ")
print(cl6.issubset(cl5))

print("Clusters Union: ")
print(cl6.union(cl5))


