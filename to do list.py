tasks=[]
def show_tasks():
    print("\n Your To-Do List: ")
    if not tasks:
        print(" - No tasks yet!")
    else:
        for i,task in enumerate(tasks, 1):
            print(f"{i}.{task}")
def add_tasks():
    task = input("Enter a new task: ")
    tasks.append(task)
def delete_tasks():
    show_tasks()
    try:
        num=int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")
def main():
    while True:
        print("\n Menu: ")
        print("1.View tasks")
        print("2.Add tasks")
        print("3.Delete tasks")
        print("4.Exit")
        choice=input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            print("Goodbyee!")
            break
        else:
            print("Invalid choice.")
if __name__=="__main__":
    main()
            
