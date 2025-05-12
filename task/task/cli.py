import json
from argparse import ArgumentParser

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.completed = False

class TaskManger:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)
    
    def add_task(self, name, deadline):
        self.tasks.append({"name":name, "deadline":deadline, "completed":False})
        self.save_tasks()
