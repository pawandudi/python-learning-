# class Student:
#     stander ="a-class"
# pawan =Student()
# rahul = Student()
# print(Student)    
# print(pawan.stander)

# class Student:
#     study=" bal niketan " # sam for all
#     def __init__( self , name , rollno):
#         self.name=name #  difrent for all
#         self.rollno=rollno
#         print("new student")  
    
#     def welcome(self):
#         print("welcome",self.name)
        
#     def get_roll_no(self):
#         return self.rollno
            
        
        


# s1= Student("pawan",21) 
# s1.welcome()
# print(s1.get_roll_no())
# print(s1.name,s1.rollno)

# s2= Student("rahul",24) 
# print(s2.name,s2.rollno)

# class Student:
#         study=" bal niketan " # same for all
#         def __init__( self , name , marks):
#             self.name=name
#             self.marks=marks
        
#         @staticmethod # to not use self word
#         def hello():
#                 print("hello")
                
#         def avg(self):
#             sum=0
#             for val in self.marks:
#                 sum+=val
#             print(self.name,"your avg", sum/5)
            
# s1=Student("pawan",[92,67,88,88,86])
# s1.avg()              
                
                
# class Bank:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no= acc_no
        
#     def debit(self,amount):
#         self.balance-=amount
#         print("$",amount ,"debited")
#         print("balance",self.balance)
        
#     def creadit(self,amount):
#         self.balance+=amount
#         print("$",amount,"creadit")
#         print("balance",self.balance)    
        
 
# acc1 =Bank(10000 ,1234)
# print(acc1.balance)
# acc1.creadit(2000)


sub1 = input("enter the subj :")
time1=input("enter hour :")
sub2= input("enter the subj :")
time2=input("enter hour :")
sub3=input("enter the sub :")
time3=input("enter hour :")

study_track=[sub1+" :"+ time1 ,sub2 +" :"+ time2, sub3 +" :"+ time3 ]
total_time=float(time1)+float(time2)+float(time3)
for i in study_track:
    print(i,"hours")
print("total study time",total_time)