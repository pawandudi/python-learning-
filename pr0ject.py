class study_tracker:
    def add_data(self):
        subject=[]
        self.subject = subject
        hourses=[]
        self.hourses = hourses
        no=int(input("no. of sub :"))
        x=0
        y=""
        for i in range(no):
            sub=input("enter sub name :")
            hour =float(input("enter hour :"))
            subject.append(sub)
            hourses.append(hour)
            x+=hour
        for i in range(no):
            print(subject[i],": ",hourses[i],"hour")
            f=0  
        while  f == 0:
            print("1.add data")
            print("2.total hour")
            print("3.show all data")
            print("4.most studed sub")
            print("5.save data")
            print("6.avg")
            print("7.min studie sub")
            print("8.exit") 
            f+=1
            choice = int(input("next task"))
            if(choice==1):
                self.add_data(self)
            elif(choice==2):
                print("total hour :",x ,"hour")
            elif(choice==3):
                for i in range(no):
                    print(subject[i],": ",hourses[i],"hour")    
            elif(choice==4):
                for i in range(no):
                    max = hourses[i]
                    if (i==0):
                        maxi=hourses[0]
                    elif (max>=maxi):
                        maxi = hourses[i]
                    
                        
                print(sub[i]," is your most stuied sub",maxi)
            elif(choice==5):
                subject=str(subject)
                hourses=str(hourses)
                name=str(input("enter name"))
                f=open("hello.py","a")  
                f.write(name)
                f.write("\n")
                f.write("subject")
                f.write("=")
                f.write(subject)
                f.write(" \n")
                f.write("hourses")  
                f.write("=")
                f.write(hourses)
                
                f.close()
            elif(choice==6):
                print("avg",(x)/ (no))
            elif(choice==7):
                for i in range(no):
                    min = hourses[i]
                    if (i==0):
                        mini=hourses[0]
                    elif (min<=mini):
                        mini = hourses[i]
                print(subject[i],"minimum studied",mini)
                
            elif (8 == choice):
                break
    
pawan=study_tracker()    
pawan.add_data()
