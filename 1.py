def employee():
    for i in range(z):
        employee_name=input('enter your name which is registed with the company')
        a=int(input("enter the no. of days u want a leave"))
        if a>10:
            print("state ur leave emergency:\noptions are:\nhospital\nfamily_gathering\nwedding or party of family/friend\nanything else")
            b=input("tell why u want a leave:")
            if b=="hospital":
                print(f"{employee_name} will get paid leave for 10daysEnjoy your paid and unpiad leaves.{a-10} days of leave will be unpaid leave")
            elif b=="family_gathering":
                print(f"{employee_name} will get a paid leave for 7days.Enjoy your paid and unpaid leaves.{a-7} days of leave will be unpaid leave")
            elif b=="wedding or party of family":
                print(f"{employye_name} will get a paid leave for 5days.Enjoy your paid and unpaid leaves.{a-5} days of leave will be unpaid leave")
            elif b=="anything else":
                print(f"{employee_name} will get a paid leave of 3days.Enjoy your paid and unpaid leaves.{a-3} days of leave will be unpaid leave ")       
        else:
            print(f"{employee_name}will get a leave wwhich is fully paid.Enjoy the leave") 
z=int(input("enter the no fo emplyess leave need:"))
print("enter your choice:\n1.Employee_leave\n2.Exit")
choice=int(input("enter your choice:"))
if choice==1:
    employee()
elif choice==2:
    exit()

