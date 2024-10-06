import csv
from db.tables.tasks_table.HandlerTasks import *

class TaskServices():

    def __init__(self) -> None:
        self.handlerTasks = HandlerTAsks()
        pass

    def showTasks(self):
        with open('./db/tables/tasks_table/tasks.csv', mode='r') as archivo:
            lector = list(csv.reader(archivo))
            headers = lector.pop(0)

            return {"headers": headers, "tasks": lector}

    def storeTask(self, task:list ):
        newId = self.handlerTasks.writeData()

        with open('./db/tables/tasks_table/tasks.csv', mode='r') as archivo:
            lector = list(csv.reader(archivo))

        with open('./db/tables/tasks_table/tasks.csv', mode='w') as archivo:
            task.insert(0, newId)
            lector.append(task)
            write = csv.writer(archivo)
            write.writerows(lector)

    def completeTask(self, id:int):
        with open('./db/tables/tasks_table/tasks.csv', mode='r') as archivo:
            lector = list(csv.reader(archivo))
            headers = lector.pop(0)
        
        for indice, row in enumerate(lector):
            idRow = int(row[0])
            if(idRow == id):
                lector.pop(indice)
                break

        with open('./db/tables/tasks_table/tasks.csv', mode='w') as archivo:
            write = csv.writer(archivo)
            lector.insert(0, headers)
            write.writerows(lector)
            
