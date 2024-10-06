import csv

class HandlerTAsks():
    def __init__(self) -> None:
        pass

    def writeData(self):
        with open('./db/tables/tasks_table/tasks_index.csv', mode='r') as archivoIndex:
            lectorIndex = list(csv.reader(archivoIndex)) 
            newId = str(int(lectorIndex[0][0]) + 1)         

        with open('./db/tables/tasks_table/tasks_index.csv', mode='w') as archivo:
            archivo.write(newId)
            return newId
