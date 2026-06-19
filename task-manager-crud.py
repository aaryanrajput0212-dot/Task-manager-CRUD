class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} | Priority: {self.priority} | {status}"


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    # ----------------------
    # FILE HANDLING
    # ----------------------

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.title},{task.priority},{task.completed}\n"
                )

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    title, priority, completed = line.strip().split(",")

                    task = Task(title, priority)
                    task.completed = completed == "True"

                    self.tasks.append(task)

        except FileNotFoundError:
            pass

    # ----------------------
    # CREATE
    # ----------------------

    def add_task(self):

        title = input("Enter Task Title: ")

        print("\nPriority Levels")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        choice = input("Choose Priority: ")

        priorities = {
            "1": "High",
            "2": "Medium",
            "3": "Low"
        }

        priority = priorities.get(choice, "Medium")

        task = Task(title, priority)

        self.tasks.append(task)

        self.save_tasks()

        print("\nTask Added Successfully!")

    # ----------------------
    # READ
    # ----------------------

    def view_tasks(self):

        if not self.tasks:
            print("\nNo Tasks Available.")
            return

        print("\n========== TASK LIST ==========")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    # ----------------------
    # UPDATE
    # ----------------------

    def update_task(self):

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_no = int(
                input("\nEnter Task Number to Update: ")
            ) - 1

            if 0 <= task_no < len(self.tasks):

                new_title = input("Enter New Title: ")

                print("\n1. High")
                print("2. Medium")
                print("3. Low")

                choice = input("New Priority: ")

                priorities = {
                    "1": "High",
                    "2": "Medium",
                    "3": "Low"
                }

                self.tasks[task_no].title = new_title
                self.tasks[task_no].priority = priorities.get(
                    choice,
                    "Medium"
                )

                self.save_tasks()

                print("\nTask Updated Successfully!")

            else:
                print("Invalid Task Number.")

        except ValueError:
            print("Please Enter a Valid Number.")

    # ----------------------
    # DELETE
    # ----------------------

    def delete_task(self):

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_no = int(
                input("\nEnter Task Number to Delete: ")
            ) - 1

            if 0 <= task_no < len(self.tasks):

                deleted_task = self.tasks.pop(task_no)

                self.save_tasks()

                print(
                    f"\n'{deleted_task.title}' Deleted Successfully!"
                )

            else:
                print("Invalid Task Number.")

        except ValueError:
            print("Please Enter a Valid Number.")

    # ----------------------
    # COMPLETE TASK
    # ----------------------

    def complete_task(self):

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_no = int(
                input("\nEnter Task Number to Complete: ")
            ) - 1

            if 0 <= task_no < len(self.tasks):

                self.tasks[task_no].completed = True

                self.save_tasks()

                print("\nTask Marked as Completed!")

            else:
                print("Invalid Task Number.")

        except ValueError:
            print("Please Enter a Valid Number.")

    # ----------------------
    # DASHBOARD
    # ----------------------

    def dashboard(self):

        total = len(self.tasks)

        completed = sum(
            task.completed for task in self.tasks
        )

        pending = total - completed

        print("\n========== DASHBOARD ==========")
        print(f"Total Tasks     : {total}")
        print(f"Completed Tasks : {completed}")
        print(f"Pending Tasks   : {pending}")


# ----------------------
# MAIN PROGRAM
# ----------------------

def main():

    manager = TaskManager()

    while True:

        print("\n" + "=" * 40)
        print("      SMART TASK MANAGER")
        print("=" * 40)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Dashboard")
        print("7. Exit")

        choice = input("\nChoose Option: ")

        if choice == "1":
            manager.add_task()

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.update_task()

        elif choice == "4":
            manager.delete_task()

        elif choice == "5":
            manager.complete_task()

        elif choice == "6":
            manager.dashboard()

        elif choice == "7":
            print("\nThank You For Using Smart Task Manager!")
            break

        else:
            print("\nInvalid Choice. Try Again.")


if __name__ == "__main__":
    main()