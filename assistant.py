print(" Hello! this is  kashu, your Python Assistant. ")
print(" You can ask me: hello,,how are you man , what is your name , Kashu ,education,school,college or bye")

subjects = []
file = open("subjects.txt","r")
for line in file:
    subjects.append(line.strip())
file.close()    
def add_subject():
    subject = input("enter the subject :")
    subjects.append(subject) 

    file = open("subjects.txt", "a")
    file.write(subject + "\n")
    file.close()

    print("Assistant : subject added succesfully !")

        

tasks =[]

file = open("study.txt","r")
for line in file:
    tasks.append(line.strip())
file.close()

while  True:
    command =input("You:").lower()

    if command =="hello":
        print("Assistant: Hello!  : ")

    elif command =="how are you man":
        print("Assistant: i am fine man.")
        
    elif command =="what is your name":
        print("Assistant: My name is Kashu.")

    elif command =="now i am calling as kashu":
        print("Assistant: okk")    

    elif command =="education":
        print("Assistant: pursuing Btech in computer science specialization in ai/ml,keep learning python,java,css,html .You are doing great.")

    elif command =="school":
        print("Assistant: St.Paul Inter College.")

    elif command =="college":
        print("Assistant :Integral University,Lucknow.")

    elif "add subject" in command:
        add_subject()

# "a " mean add in the end (append)
        print("Assistant: Subject added succesully!")

    elif"view subjects" in command:
        print("your subjects:")

        for i in range(len(subjects)):
            print( i+1,"-",subjects[i])
 
    elif"delete subject" in command:
        try:
            subject_number =int(input("enter the subject number"))

            index = subject_number -1

            del subjects[index]

            file = open("subjects.txt","w")

            for subject in subjects:
                file.write(subject+"\n")
            file.close()

            print("Assistant: subjects deleted successfuly!")

        except:
            print("Assistant: sorry , something went wrong with subject number!")


       
#w will replace the curent  subject file and  update it after deleting the subject


    elif"clear subjects" in command:
        subjects.clear()

        file = open("subjects.txt","w" )
        file.close()
        print("Assistant: all subjects have been cleared successfully !")        

    elif "add task" in command:
        task=input("enter your study task: ")
        priority =input("enter priority(high/medium/low):").lower()
        if priority not in["high","medium","low"]:
            print("Assistant: invalid priority! please choose high,medium or low.")
        tasks.append(task + "/" + priority)

        file =  open("study.txt", "a")
        file.write(task + "/" + priority +"\n")
        file.close()
        
        print("Assistant: study task added succesfully! ") 



       


    elif"view task" in command:
        print("your Study task")

        for i in range(len(tasks)):
            print(i+1,"$",tasks[i])

    elif"high priority tasks" in command:
        print("your high priority tasks: ")

        for i in range(len(tasks)):
            if"/high" in tasks[i]:
                print(i + 1 ,"-" , tasks[i]) 

    elif"medium priority tasks" in command:
        print("your medium priority tasks: ")

        for i in range(len(tasks)):
            if"/medium" in tasks[i]:
                print(i+1 , "-" , tasks[i])

    elif"low priority tasks" in command:
        print("your low priority tasks:")

        for i in range(len(tasks)):
            if"/low" in tasks[i]:
                print(i+1 ,"-" ,tasks[i])                               

    elif"study progress" in command:
        total_tasks =len(tasks)
        completed_tasks = 0

        for task in tasks:
            if "complete button" in task:
                completed_tasks=completed_tasks + 1
        print("Assistant: study progress")
        print("total task:" ,total_tasks)
        print("completed tasks:",completed_tasks)
        print("remaining tasks:",  total_tasks - completed_tasks)               


    elif "delete task" in command:
           try:
            task_number =int(input("enter the task number: "))
            index = task_number -1
            print("Before delete:",tasks)
            del tasks[index]
            print("After delete:",tasks)
    
            file = open("study.txt","w")
            for task in tasks:
                file.write(task,"\n")
    
            file.close()   
            print("your task has been delete succesfully! ")  
    
           except:
               print("something went wrong with task number! ") 


    elif"clear tasks" in command:
        tasks.clear()

        file = open("study.txt" ,"w")
        file.close()

        print("Assistant: All tasks have been cleares!")       

    elif"complete task" in command:
        try:
            
            task_number =int(input("enter the task number :"))
            index = task_number -1
            if " complete   button " not in tasks[index]:
                tasks[index] = tasks[index] + "complete button"

                file = open("study.txt", "w")
                for task in tasks:
                    file.write(task + "\n")
                file.close()

                print(" Assistant : Task completed !")

            else:
                print(" Assistant : this task is already completed !")

        except:
            print(" Assistant :  sorry, something went wrong with the task number .!")
                   

       
    
    elif "help" in command:
        print("Assistant: you can use these commands :")
        print("- add subejcts")
        print("- view subejcts")
        print("- add task")
        print("- view tasks")
        print("- delete task")
        print("- complete task")
        print("- bye")


    elif "bye" in command or "exit" in command:
        print("Assistant: Goodbye ! keep  learning and study hard !")
        break






    
        