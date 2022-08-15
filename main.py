print("""Hi buddy
write hint to know this program""")
tasks=[]
person=[]
while True:
    msg=input()
    
    if msg=="exit" : break

    if msg=="hint" :
        print("add : To add task\n" +
        "remove : To remove task\n" +
        "tasks : To see availble task\n" +
        "exit : Exit")

    if msg=="add" :
        print("Name :")
        person.append(input())
        print("her/his task :")
        tasks.append(input())

    if msg=="remove" :
        if len(person)==0 :
            print("There aren't any tasks")
        else :
            print("name :")
            p=input()
            i=0
            Len=len(person)
            while(i< len(person)) :
                if person[i]==p :
                    del person[i]
                    del tasks[i]
                    break
                i +=1
            if i== Len :
                print("We don't have this person")        

    if msg=="tasks" :
        j=0
        while(j< len(person)) :
            print( person[j] + " : " + tasks[j] )   
            j +=1 
        if len(person)==0 :
            print("There aren't any tasks")         