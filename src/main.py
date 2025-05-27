from datetime import datetime
import csv

tasks=[]
csv_file="tasks.csv"
def add_task(task,priority):
    task_object={"task":task,"is_completed":False,"time":datetime.now(),"priority":priority}              
    tasks.append(task_object)
    # print(tasks)
    

def list_task():
    if not tasks:                  
        print("no task")
    else:
        print("tasks list")
        for index, task in enumerate (tasks):
            index=index+1
            if task['is_completed']==False:

                print(f"{index}:{task.get('task')} || completed: {task.get('is_completed')} ")
            

def mark_completed():
    index=int(input("Please enter the number of the completed task."))
    index=index-1
    if index>=0 and index<len(tasks):
        tasks[index]['is_completed']=True

          
            

def delete_task():
    index=int(input("enter the task number to delete: "))
    index=index-1                                   
    if 0 <= index < len(tasks):
        deleted_task=tasks.pop(index)
        print(f"Deleted task: {deleted_task['task']}")
    else:
        print("please enter the valid task number")


if __name__=="__main__":

    while True:
        print("Task Manager")
        print("1.Add task")
        print("2.List task")
        print("3.mark completed")
        print("4.Delete task")
        print("5.exit")

        
        choice=input("Enter the choice: ")

        if choice=="1":
            user_task=input("Enter the task: ")
            task_priority=input("Enter the priority level: ")
            add_task(user_task,task_priority)

        elif choice=="2":
            list_task()

        elif choice=="3":
            mark_completed()

        elif choice=="4":
            delete_task()

        else:
            print("exit")
            break
      

