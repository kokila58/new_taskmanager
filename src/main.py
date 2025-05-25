from datetime import datetime
tasks=[dict]
def add_task(task,priority):
    task_object={"task":task,"is_completed":False,"time":datetime.now(),"priority":priority}              
    tasks.append(task_object)
    print(tasks)

if __name__=="__main__":
    user_task=input("Enter the task: ")
    task_priority=input("Enter the priority level: ")
    add_task(user_task,task_priority)
      