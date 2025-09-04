def to_do():
    for i in range(0,n):
        task=input("enter the task which u want to do:")
        l.append(task)
        print("ur tasks are: ",l)
        choice=int(input("if u have completed any task then press 1 or press 0 to exit:"))
        if choice==1:
            def completed():
                task=input("inout the task which u have completed:")
                if task in l:
                    l.remove(task)
                    print("comgratulations.You have do the task successfully.\nThe task done is:",task)
                    print("Now the remaining tasks are:",l)
                else:
                    print("U didnt add anu task like that,\Check it once again\nor add the task first")
            completed()
        elif choice==2:
            def unfinshed():
                print("there are remianing tasks:",l)
            unfinshed()
        else:
            print("thank u for using this to-do app")
            exit()

n=int(input("if u want to add more task then press 1 or press"))
l=[]
to_do()
