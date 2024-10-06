from src.app.controllers.task.TaskController import *
from src.app.views.tableView import tableView
import os

class Index():
    def __init__(self) -> None:
        createTaskServices = TaskController()

        while(True):
            os.system('clear')
            inputUser =  input('1. Mostrar tareas\n2. Crear Tareas\n3. Exit\n-')

            if(inputUser == '1'):
                tasks = createTaskServices.index()
                tableView(tasks['headers'], tasks['tasks'])
               
                inputUserIn1 = input('M: Modificar tarea\nS: Mover tarea\nE: Eliminar tarea\n-')
                # if(inputUserIn1 == 'E'):
                #     pass
                if(inputUserIn1.lower() == 'e'):
                    idProccesInput = int(input('Id de la tarea a eliminar: '))
                    createTaskServices.complete(idProccesInput)

            if(inputUser == '2'):
                newTask = input('Introduzca una tarea, Titulo y Descripcion, separado por comas: ').split(', ')
                newTask.append('por hacer')
                createTaskServices.store(newTask)


            if(inputUser == '3'):
                break

            input('enter para continuar...')

def main():
    index = Index()

if __name__ == "__main__":
    main()