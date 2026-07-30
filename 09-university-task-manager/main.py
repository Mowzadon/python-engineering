


tasks = []

def add_task(tasks): 
    """
    Creates a new task from user input and adds it to the task list.

    Args: 
        tasks (list): 
            List containing task dictionaries. 
    """

    description = input("Task description: ").strip().title()
    due_date = input("due date: ").strip()
    course = input("Course: ").strip().upper()
    priority = input("Priority: ").strip().title()

    new_task = {
        "description": description, 
        "due_date": due_date, 
        "course": course,
        "priority": priority, 
        "completed": False,
    }

    tasks.append(new_task)
    print("Task added.")

def view_tasks(tasks): 
    """
    Displays every task in the task list.

    Args: 
        tasks (list): 
            List containing task dictionaries. 
    """
    if not tasks: #Is the list empty? 
        #tasks = [] is false, so
        #if not tasks == True
        print("No tasks found.")
        return #Exit the function at this line. 

    for index, task in enumerate(tasks, start = 1): #for task in tasks: (returns each indexed position)
        #enumerate creates pairs(tasks, index(1.... n))
        print(
            f"{index}. "
            f"{task['description']} | "
            f"{task['course']} | "
            f"Due: {task['due_date']} | "
            f"Priority: {task['priority']} | "
            f"Completed: {task['completed']}"
        )

add_task(tasks)
view_tasks(tasks)




