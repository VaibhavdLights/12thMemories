#modules/software to install
#pip
#mysql
#pymysql


#⛾⛳☕☎☑☒
#HOTEL DETAILS
    #☑ ⛳HOTEL AKRVP
    #☑ THE HOTEL IS SITUATED UP ABOVE IN SPACE
    #☑ THE MODE OF GOING TO HOTEL IS BY INTERGALECTIAL LIFT DEVELOPED BY SPACEX
    #☑ THE HOTEL IS FULLY ARTIFICIAL INTELLIGENCE
    #☑ THERE ARE SO MANY OTHER FEATURES
    #☑ FOR MORE INFORMATION CALL ☎0000000000
from time import sleep
from datetime import datetime
date_format = "%Y-%m-%d"
#Function to add guest
def addGuest():
    mycursor = conn.cursor()
    query="select guestID from ehm order by guestID desc limit 1"
    query1="select guestID from ehmold where guestID is not null order by guestID desc limit 1 "
    mycursor.execute(query)
    row = mycursor.fetchone()
    if mycursor.rowcount==0:
        guestID=1
    else:
        ID=row["guestID"]
        mycursor.execute(query1)
        row1 = mycursor.fetchone()     
        ID1=row1["guestID"]
        if ID>=ID1:
            guestID=ID+1
        else:
            guestID=ID1+1
    print("Guest Number : ",guestID)
    gname=input("Enter the name of guest  ►►►  ")
    add=input("Enter the address of guest  ►►►  ")
    mno=input("Enter the mobile number of guest  ►►►  ")
    Aadhar=input("Enter the aadhar number of guest  ►►►  ")
    CIdate=input("Enter the check in date  ►►►  ")
    CItime=input("Enter the check in time  ►►►  ")
    COdate=input("Enter the check out date  ►►►  ")
    COtime=input("Enter the check out time ►►►  ")
    Rtype,amt,n=RoomType(CIdate,COdate)
    Rno=allotRoom(Rtype)
    print("You have been alloted room number ► ",Rno)
    print ("Do you want to check in (Y/N)? ►►► ")
    query = "insert into ehm values({},'{}','{}','{}','{}','{}','{}',{},{},'{}','{}',{})"
    mycursor.execute(query.format(guestID,gname,add,mno,Aadhar,CIdate,CItime,Rno,Rtype,COdate,COtime,amt))
    c=input()
    if c in['y','Y']:
        conn.commit()
        print("Data saved successfully !!!")
        print ("Amount payable for your stay of ",n," days is ► ",amt)
    else:
        conn.rollback()
        print("NO records saved !!!")
    input("Press any key to continue ►►► ")
#Function To get roomtype and payable amount
def RoomType(CIdate,COdate):
    Rtype=int(input("Enter the room type ►\n1 for Single \n2 for Double \n3 for Suit \n4 for Murphy\n►►►  "))
    n1 = datetime.strptime(CIdate, date_format)
    n2 = datetime.strptime(COdate, date_format)
    n=n2-n1
    n3=int(n.days)
    if Rtype==1:
        amt=n3*5000
    elif Rtype==2:
        amt=n3*15000
    elif Rtype==3:
        amt=n3*30000
    elif Rtype==4:
        amt=n3*45000
    else:
        print("Please enter one of the above mentioned room types ►►► ")
        RoomType(CIdate,COdate)
    return (Rtype,amt,n3)
#Function to allot room to the guests
def allotRoom(Type):
    mycursor=conn.cursor()
    query="select Rno from ehm where Rtype={}"
    mycursor.execute(query.format(Type))
    row=mycursor.fetchall()
    n=mycursor.rowcount
    if Type==1:
        s=101
    elif Type==2:
        s=201
    elif Type==3:
        s=301
    elif Type==4:
        s=401
    if n==0:
        return s
    else:
        for i in range(n):
            if s!=row[i]["Rno"]:
                print (s)
                return s
            else:
                s+=1
        else:
            return s
#Function to display the details of all guests
def qallGuest():
    mycursor=conn.cursor()
    
    query="select * from ehm"
    mycursor.execute(query)
    count=mycursor.rowcount
    if count==0:
        print('No Guest Found !!!')
    else:
        print('Guest Details are ►►► ')
        rows=mycursor.fetchall()
        print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY".ljust(15))
        print(132*'⚍')
        ctr=1
        for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))
              ctr+=1
              if ctr%30==0:
                  input('Press any key to see more ►►►')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY".ljust(15))
                  print(132*'⚍')
#Function to display the details guest id wise
def qgidwise():
    mycursor=conn.cursor()
    gid=input("Enter Guest ID ►►► ")
    query="select * from ehm where GuestID={}"
    mycursor.execute(query.format(gid))
    count=mycursor.rowcount
    if count==0:
        print('No Guest Found 1!!')
    else:
        print('Guest Details are ►►► ')
        rows=mycursor.fetchall()
        print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
        print(132*'⚍')
        ctr=1
        for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))              
              ctr+=1
              if ctr%30==0:
                  input('Press any key to see more ►►► ')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
                  print(132*'⚍')
#Function to display details check in date wise
def qcheckinwise():
    mycursor=conn.cursor()
    cidate=input("Enter Check in Date ►►► ")
    query="select * from ehm where cidate='{}'"
    mycursor.execute(query.format(cidate))
    count=mycursor.rowcount
    if count==0:
        print('No Guest Found !!!')
    else:
        print('Guest Details are ►►► ')
        rows=mycursor.fetchall()
        print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
        print(132*'⚍')
        ctr=1
        for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))            
              ctr+=1
              if ctr%30==0:
                  input('Press any key to see more ►►► ')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
                  print(132*'⚍')
#Function to display details check out date wise 
def qcheckoutwise():
    mycursor=conn.cursor()
    codate=input("Enter Check out Date ►►► ")
    query="select * from ehm where codate='{}'"
    mycursor.execute(query.format(codate))
    count=mycursor.rowcount
    if count==0:
         print('No Guest Found !!!')
    else:
         print('Guest Details are ►►► ')
         rows=mycursor.fetchall()
         print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
         print(132*'⚍')
         ctr=1
         for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))
              ctr+=1
              if ctr%30==0:
                  input('Press any key to see more ►►► ')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
                  print(132*'⚍')
#Function to display details room number wise
def qrnowise():
    mycursor=conn.cursor()
    rno=input("Enter Room Number ►►► ")
    query="select * from ehm where rno={}"
    mycursor.execute(query.format(rno))
    count=mycursor.rowcount
    if count==0:
        print('No Guest Found !!!')
    else:
        print('Guest Details are ►►► ')
        rows=mycursor.fetchall()
        print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
        print(132*'⚍')
        ctr=1
        for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))              
              if ctr%30==0:
                  input('Press any key to see more ►►► ')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
                  print(132*'⚍')
#Function to update check out date
def updatecheckout():
    mycursor=conn.cursor()
    r=int(input("Enter room number of guest ►►► "))
    query="update ehm set COdate='{}' where Rno={}"
    query2="select Rno from ehm"
    mycursor.execute(query2)
    row=mycursor.fetchall()
    n=mycursor.rowcount
    flag=0
    for i in range(n):
        if row[i]["Rno"]==r:
            flag=1
    if flag==0:
        print("No guest found with room number ",r,"\nPlease enter correct room number !!!")
        updatecheckout()
    else:
        newdate=input("Enter new checkout date ►►► ")
        c=input("Are you sure to modify checkout date(Y/N)? ►►► ")
        if c in ['y','Y']:
            mycursor.execute(query.format(newdate,r))
            conn.commit()
            query3="select * from ehm where Rno={}"
            mycursor.execute(query3.format(r))
            row=mycursor.fetchall()
            cin=str(row[0]["CIDATE"])
            n4 = datetime.strptime(cin, date_format)
            n5 = datetime.strptime(newdate, date_format)
            n0=n5-n4
            n6=int(n0.days)
            RT=row[0]["RTYPE"]
            amt=0
            if RT==1:
                amt=n6*5000
            elif RT==2:
                amt=n6*15000
            elif RT==3:
                amt=n6*30000
            elif RT==4:
                amt=n6*45000
            query4="select AMT from ehm where Rno={}"
            mycursor.execute(query4.format(r))
            row=mycursor.fetchall()
            inamt=row[0]["AMT"]
            query5="update ehm set AMT={} where Rno={}"
            mycursor.execute(query5.format(amt,r))
            print("Extra amount added is ► ",amt-inamt)
            print ("Your new amount payable for your stay of ", n6 ," days is ► ",amt)
            input("Press any key to go back to main menu ►►► ")
#Function to refresh database            
def refresh():
    mycursor=conn.cursor()
    query3="insert into ehmold select * from ehm where curdate()>CODATE and current_time()>COTIME"
    mycursor.execute(query3)
    conn.commit()
    query4="delete from ehm where curdate()>CODATE and current_time()>COTIME"
    mycursor.execute(query4)
    conn.commit()
    loading="R E F R E S H I N G..."
    for i in range(22):
        print(loading[i],end=''); sleep(0.2)
    input("\nPress any key to continue to main menu ►►► ")    
#function to display data of old customers
def oldcus():
     print("Details of old guests ►►► ")
     mycursor=conn.cursor()
    
     query="select * from ehmold"
     mycursor.execute(query)
     count=mycursor.rowcount
     if count==0:
        print('No Guest Found !!!')
     else:
        print('Guest Details are ►►► ')
        rows=mycursor.fetchall()
        print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
        print(132*'⚍')
        ctr=1
        for row in rows:
              print(str(row["GuestID"]).center(7),str(row["GNAME"]).ljust(20),str(row["ADDR"]).ljust(25),str(row["MNo"]).ljust(15),str(row["AADHAR"]).ljust(15),str(row["CIDATE"]).ljust(15),str(row["CITIME"]).ljust(15),str(row["RNo"]).ljust(5),str(row["RTYPE"]).center(10),str(row["CODATE"]).ljust(15),str(row["COTIME"]).ljust(15),str(row["AMT"]).ljust(15))
              ctr+=1
              if ctr%30==0:
                  input('Press any key to see more ►►► ')
                  print("GuestID".center(7),"GNAME".ljust(20),"ADDRESS".ljust(25),"MOB NO".ljust(15),"AADHAR NO".ljust(15),"CHECK IN DATE".ljust(10),"CHECK IN TIME".ljust(15),"ROOM NO".ljust(5),"ROOM TYPE".center(10),"CHECK OUT DATE".ljust(15),"CHECK OUT TIME".ljust(15),"PAY AMOUNT".ljust(15))
                  print(132*'⚍')
     input(print("Press any key to continue ►►►"))
#function to see room specifications
def roomspec():
    mycursor=conn.cursor()
    rtype=int(input("Enter room type \n1.For Single\n2.For Double\n3.For Suit\n4.For Murphy\n"))
    query="select * from room where Rtype={}"
    print("The details of the room are ►►► \n")
    mycursor.execute(query.format(rtype))
    rows=mycursor.fetchall()
    print("Room Type".ljust(15),"Beds".ljust(10),"AC".ljust(10),"Wi-Fi".ljust(10),"AI".ljust(10),"Rent(per night)".ljust(10))
    print(str(rows[0]["Rtype"]).ljust(15),str(rows[0]["Beds"]).ljust(10),str(rows[0]["AC"]).ljust(10),str(rows[0]["Wifi"]).ljust(10),str(rows[0]["AI"]).ljust(10),str(rows[0]["Rent"]).ljust(10))
    input(print("Enter any key to continue ►►► "))
#MAIN MENU
def mainmenu():
    print('\n⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶⚶')
    print("\n\t\t\t\t\t\t\t\t\t⇛EDITH HOTEL MANAGEMENT SYSTEM⇚")
    print("\t\t\t\t\t\t\t\t\t    ⇝POWERED BY AKRVPTECH⇜")
    print("\n⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟⚞⚟")
    print("1.ADD NEW GUEST( ☛ 1 ) ►►► ")
    print("2.View room specifications( ☛ 2 ) ►►► ")
    print("3.Query( ☛ 3 ) ►►► ")
    print("4.Update check out time( ☛ 4 ) ►►► ")
    print("5.Display data of old customers( ☛ 5 ) ►►► ")
    print("6.Refresh database( ☛ 6 ) ►►► ")
    print("7.Exit( ☛ 7 ) ►►► ")
    ch=int(input("Enter your Choice  ►►► "))
    if ch==1:
        addGuest()
    elif ch==2:
        roomspec()
    elif ch==3:
        print("\n☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶")
        print("QUERY MENU")
        print("⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊")
        print("-----------------------------------------------------------------Guests---------------------------------------------------------------------------------------")
        print("1.All Guest alphabetical( ☛ 1 ) ►►► ")
        print("2.Guest ID wise( ☛ 2 ) ►►► ")
        print("3.Check in wise( ☛ 3 ) ►►► ")
        print("4.Check out wise( ☛ 4 ) ►►► ")
        print("5.Room number wise( ☛ 5 ) ►►► ")
        print("6.Back to main....( ☛ 6 ) ►►► ")
        ch1=int(input("Enter your choice  ►►► "))
        if ch1==1:
            qallGuest()
        elif ch1==2:
            qgidwise()
        elif ch1==3:
            qcheckinwise()
        elif ch1==4:
            qcheckoutwise()
        elif ch1==5:
            qrnowise()
        elif ch1==6:
            mainmenu()
        else:
            print("Wrong choice ⚠ !!! <--BACK TO MAIN MENU -->")
            mainmenu()
    elif ch==4:
         updatecheckout()
    elif ch==5:
         oldcus()
    elif ch==6:
         refresh()
    elif ch==7:
        status = input("Do you really want to quit(Y/N)?....")
        if status in ['y','Y']:
            sys.exit()
        else:
            pass
    else:
        print ("Wrong choice ⚠ !!! Try again!!!")
        mainmenu()
#Main Program
import pymysql as sql
import sys
conn=sql.connect(user="root",password="toor",host="localhost")
mycursor=conn.cursor()
choice=input("Do you want to create environment for hotel management software (Y/N)? \n ►►► ")
if choice in ['Y','y']:
    mycursor.execute("create database if not exists EDITH")
    mycursor.execute("use EDITH")
    #mycursor.execute(query.format(guestID,gname,add,mno,Aadhar,CIdate,CItime,Rno,Rtype,COdate,COtime,amt))
    mycursor.execute("create table if not exists ehmold(GuestID int(7) primary key,GNAME varchar(25),ADDR varchar(100),MNo varchar(12),AADHAR varchar(12),CIDATE date,CITIME time,RNo int(4),RTYPE int(2),CODATE date, COTIME time, AMT int(15))")      
    mycursor.execute("create table if not exists room(Rtype int(10), Beds int(3),AC varchar(3) ,Wifi varchar(4),AI varchar(4),Rent int(10))")
    mycursor.execute("insert into room values (1,1,'YES','NO','NO',5000)")
    conn.commit()
    mycursor.execute("insert into room values (2,2,'YES','YES','YES',15000)")
    conn.commit()
    mycursor.execute("insert into room values (3,4,'YES','YES','YES',30000)")
    conn.commit()
    mycursor.execute("insert into room values (4,3,'YES','YES','YES',45000)")
    conn.commit()
    mycursor.execute("create table if not exists ehm(GuestID int(7) primary key,GNAME varchar(25),ADDR varchar(100),MNo varchar(12),AADHAR varchar(12),CIDATE date,CITIME time,RNo int(3),RTYPE int(2),CODATE date, COTIME time, AMT int(15))")
    mycursor.execute("insert into ehmold values (0,'YourAI','00000000','0000000000','000000000000','0000-00-00','00:00:00',0000,0,'0000-00-00','00:00:00',0000)")
    conn.commit()
else:
    print('Exitting !!!')
lk=['HOTEL DETAILS','☑ ⛳HOTEL AKRVP','☑ THE HOTEL IS SITUATED UP ABOVE IN SPACE','☑ THE MODE OF GOING TO HOTEL IS BY INTERGALECTIAL LIFT DEVELOPED BY SPACEX','☑ THE HOTEL IS FULLY ARTIFICIAL INTELLIGENCE','☑ THERE ARE SO MANY OTHER FEATURES','☑ FOR MORE INFORMATION CALL ☎0000000000]']
for i in range(len(lk)):
    print(lk[i],end='\n'); sleep(0.2)
conn=sql.connect(user="root",password="toor",host="localhost",database="EDITH",cursorclass=sql.cursors.DictCursor)
while True:
    mainmenu()
