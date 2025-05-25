from datetime import datetime
tasks=[dict]
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

if __name__=="__main__":
    while True:
        user_task=input("Enter the task (or type exit): ")
        if user_task=="exit":
            break
        task_priority=input("Enter the priority level: ")
        add_task(user_task,task_priority)
        

    list_task()
      