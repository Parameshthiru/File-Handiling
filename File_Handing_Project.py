
'''File handing project to do add, show, search, update, delete the data and exit from the file''' 

import os       #To modify or create in operation system 
while(True):    #To create a infinity loop
    print("\n********************************************************")
    print("Student Management System")
    print("********************************************************")
    print("PRESS 1 : To Add student data")
    print("PRESS 2 : To Display data all the data")
    print("PRESS 3 : To Search student by Reg_no")
    print("PRESS 4 : To Update student data")
    print("PRESS 5 : To Delete Student data by Reg_no")
    print("PRESS 6 : To Exit")
    print("********************************************************")

    n = int(input("\tENTER YOUR CHOICE(1 - 6): "))      #Getting input from user
    if(n==6):       
        print("---------------------------------------------")
        print("\t~~~~~~~ Thank you ~~~~~~~")
        print("---------------------------------------------")
        break       #To exit from the loop
    elif(n==1):
        print("---------------------------------------------")
        print("\tEnter Student Details")
        print("---------------------------------------------")
        r = input("\tEnter Reg_No: ")
        n = input("\tEnter Name: ")
        age = input("\tEnter Student Age: ")
        mail = input("\tEnter Mail_id: ")
        mob = input("\tEnter Mobile_No: ")
        print("Student data Added successfully")
        print("--------------------------------------------------\n")
        f = open("file_handling1.txt", "a")     #To opening the file to append operation
        f.write(r+" : "+n+" : "+age+" : "+mail+" : "+mob+"\n")  #writing the inputs got form the user
        f.close()   #To close the file
    elif(n==2):
        print("--------------------------------------------------")
        print("\tOVERALL STUDENT DETAILS IN THE FILE")
        print("--------------------------------------------------")
        print("ROLL : NAME : AGE : MAIL_ID : MOBILE_NO.")
        print("--------------------------------------------------")
        f = open("file_handling1.txt", "r")     #Oening file to do read operation
        while(True):
            d = f.readline()
            l = len(d)
            if(l==0):  #Condition if the lines in file in zero -- No records --
                print("\t\tNo Records exist\n\n")
                print("--------------------------------------------------\n")
                break
            print(d.strip())
        f.close()
    elif(n==3):
        search = input("Enter Student Reg_No: ")
        f = open("file_handling1.txt", "r")
        flag = 0
        while(True):
            t = f.readline()
            l = len(t)
            if(l == 0):
                break
            g = t.split(" : ")  #To remove : from each line
            if(g[0] == search):
                print("\n ~~~~~ Record found ~~~~~\n")
                print("-----------------------------------------------------------------------")
                print("\t\tReg_No. :", g[0])
                print("\t\tName :", g[1])
                print("\t\tAge :", g[2])
                print("\t\tEmail :", g[3])
                print("\t\tMobile num :", g[4])
                print("-----------------------------------------------------------------------")
                flag = 1
                break
        if(flag ==0):
            print("********\tRecord not found\t********")
        f.close()
    elif(n==4):
        h=0
        search = input("Enter student reg num : ")
        f = open("file_handling1.txt", "r")
        tt = open("temp.txt","w")   
        flag = 0
        while(True):
            t = f.readline()
            l = len(t)
            if(l==0):
                break
            g = t.split(" : ")
            if(g[0]== search):
                print("Current details of Reg_No: ",search,"\n", t)
                print("---------------------------------------------------")
                newreg = input("To UPDATE the Reg_No? Enter new value or Press ENTER to continue with the same")
                newname = input("To UPDATE the Name? Enter new value or Press ENTER to continue with the same")
                newage = input("To UPDATE the age? Enter new value or Press ENTER to continue with the same")
                newmail = input("To UPDATE the mail_id? Enter new value or Press ENTER to continue with the same")
                newmob = input("To UPDATE the mobile_number? Enter new value or Press ENTER to continue with the same")
                if(len(newreg)== 0):
                    newreg = g[0]
                if(len(newname)== 0):
                    newname = g[1]
                if(len(newage)== 0):
                    newage = g[2]
                if(len(newmail)== 0):
                    newmail = g[3]
                if(len(newmob)== 0):
                    newmob = g[4]
                tt.write(newreg+" : "+newname+" : "+newage+" : "+newmail+" : "+newmob+"\n")
                h = 1
            else:
                tt.write(t)
        f.close()
        tt.close()
        if(h==1):
            print("********\tRecord updated\t********")
            os.remove("file_handling1.txt")
            os.rename("temp.txt","file_handling1.txt")
        elif(h==0):
            print("********\tNo Such Record Exist\t********")
    elif(n==5):
        search = input("Enter reg no.: ")
        f = open("file_handling1.txt", "r")     #opening file to do read operation
        tt = open("temp.txt","w")       #Creating a temprary file to do write operation
        h= 0
        flag = 0
        while(True):
            t = f.readline()
            l = len(t)
            if(l==0):
                break
            g = t.split(' : ')
            if(g[0]!= search):
                tt.write(t)
            if(g[0] == search):
                h = 1
        f.close()
        tt.close()
        if(h==1):
            print("********\tRecord Deleted\t********")
            os.remove("file_handling1.txt")
            os.rename("temp.txt","file_handling1.txt")
        elif(h==0):
            print("********\tNo Such Record Exist\t********")
