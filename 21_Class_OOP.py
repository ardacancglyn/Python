#Class
print("Class-Part: ")
class human():
    weight=85
    height=180
    gender="male"


human_1=human()
human_2=human()
print(human_1.gender)
#Human_1 and human_2 same,but we want not same both of them so (OOP)


#OOP
print("OOP-Part: ")

class humans():
    
    def __init__(self,hweight,hheight,hgender):
        self.w=hweight
        self.h=hheight
        self.g=hgender
humans1=humans(80,165,"male")
print(humans1.w,humans1.h,humans1.g)
humans2=humans(50,160,"female")
print(humans2.w,humans2.h,humans2.g)
#and now humans1 and humans2 not same :) 
