tasks = []
def add_task():
  task = input("Enter a new task = ")
  tasks.append(task)
  print("Task added successfully.")
  
def view_tasks():
  if len(tasks) == 0:
    print("\nNo Tasks present.")
  else:
    print("List of tasks.")
    for i,task in enumerate(tasks):
      print(f'{i+1}. {task}')
  
def delete_task():
  if len(tasks) == 0:
    print("No tasks to delete: ")
  else:
    for i,task in enumerate(tasks):
      print(f'{i+1}. {task}')
    choice = int(input("Enter the number of task you want to delete = "))
    if 0 < choice <= len(tasks):
      del tasks [choice-1]
      print("\nTask Deletion successful.")
    else:
      print("\nInvalid task number.")
    
def main():
  while True:
    print("\n===== To-Do-List Application =====")
    print("1. Add Tasks")
    print("2. Delete Tasks")
    print("3. View Tasks")
    print("4. Quit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
      add_task()
    if choice == 2:
      delete_task()
    if choice == 3:
      view_tasks()
    if choice == 4:
      print("Thanks for using the To-Do-List Apllication.")
      break
    
if __name__ == '__main__':
  main()