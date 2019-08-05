#Print Open (.txt) and Write     
#(.txt same folder,example:C:\Users\Your user ıd\.spyder-py3)

#2 Way
#1-
folder_txt=open("python.txt","w") #   "w" =write
print("Hello",file=folder_txt,flush=True)


#2-
folder_txt=open("python.txt","w")
print("World",file=folder_txt)
folder_txt.close()




















