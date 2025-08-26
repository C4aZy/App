def employee():
    a=int(input("enter the no. of days u want a leave"))
    b=input("state ur leave emergency")
    if a>10:
        if b=="hospital":
            print(f"u will get paid leave for 10day.sEnjoy your paid and unpiad leaves.{a-10}days of leave will be unpaid leave")
        else:
            print(f"u will get a paid leave for 5days.Enjoy your paid and unpaid leaves.{a-5}days of leave will be unpaid leave")
    else:
        print("ur leave is fully paid.enjoy the leave") 
employee()  