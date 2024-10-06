from src.app.controllers.task.services.TaskServices import *

class TaskController():

    def __init__(self) -> None:
        self.taskServices = TaskServices()
        pass

    def index(self):
        try:
            return self.taskServices.showTasks()
        except:
            print('error')

    def store(self, task:list):
        try:
            self.taskServices.storeTask(task)
        except:
            print('error')

    def complete(self, id:int):
        try:
            self.taskServices.completeTask(id)
        except(KeyError):
            print(KeyError)
