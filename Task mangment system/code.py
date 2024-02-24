class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Due Date: {self.due_date}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, priority, due_date)
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            print("\nAll Tasks:")
            task_manager.view_tasks()

        elif choice == "3":
            title = input("Enter title of task to delete: ")
            task_manager.delete_task(title)
            print("Task deleted successfully!")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
