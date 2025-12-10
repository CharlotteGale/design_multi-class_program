class ToDo:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if not isinstance(task, str):
            raise TypeError("Enter a valid task string")
        
        if task == "":
            raise ValueError("Enter a task")
        
        self.task_list.append(task)