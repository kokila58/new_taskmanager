from datetime import datetime
tasks=[]
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
            print(task)

def delete_task():
    index=int(input("enter the task number to delete: "))
    if 0 <= index < len(tasks):
        deleted_task=tasks.pop(index)
        print(f"Deleted task: {deleted_task['task']}")



if __name__=="__main__":

    while True:
        print("Task Manager")
        print("1.Add task")
        print("2.List task")
        print("3.Delete task")
        print("4.exit")
        
        choice=input("Enter the choice: ")

        if choice=="1":
            user_task=input("Enter the task: ")
            task_priority=input("Enter the priority level: ")
            add_task(user_task,task_priority)

        elif choice=="2":
            list_task()

        elif choice=="3":
            delete_task()

        else:
            print("exit")
            break
      

