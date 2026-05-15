# class Student:
#         __stander ="a-class" # to hide the details 
#         cast = "jaat"
# pawan =Student()
# rahul = Student()
# print(Student)    
# # print(pawan.__stander)
# # del rahul # to delete
# # print(pawan)
# # print(rahul)  

# class school (Student): # inherdatary
#     def __init__(self,name):
#           self.name=name
#           print(self.cast)
          
          
# sh1=school("rana")
# class a:
#     valua ="lakshy"
# class b:
#     valb="dev"

# class c(a,b):
#     valc="vansh"
     
# c1=c()

# print(c1.valua)    


# class a:     
#         self.type=type
        
#     def open(self):
#         print("start")
        
        
# class b(a):
#     valb="dev"
#     def __init__(self,name,type):
#         super().__init__(type) #use parent type
#         self.name=name
#         super().open()
        
        
# david = b("googins","marathon")
# print(david.type)
         
# class person:
#     name="pawan"
    
#     def change(self , name):
#         self.__class__.name = name
#         # person.name=name # method of change main name 
#             @classmethod  # also modify class
# def change_name(cls,name):
#     cls.name=name
# p1=person()
# p1.change("rahul")
# print(p1.name)

# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
          
#     @property # for latest change this also change
#     def percentage(self):
#         return (self.phy+ self.chem + self.math)/3
    
# s1=student(90,98,95)
# print(s1.percentage)  
# s1.phy=98
# print(s1.percentage)

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         print((22/7)*self.radius**2)
        
# c1=circle(9)    
# c1.area()
 
# class Order:
#     def __init__(self,item,prise):  
#         self.iten=item
#         self.prise=prise
    
#     def __gt__( self , odr2 ):
#         return self.prise > odr2.prise
      
# ord1= Order("lux",20) 
        
# odr2= Order("t",10)

# print(ord1 > odr2)

