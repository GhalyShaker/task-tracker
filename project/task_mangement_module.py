from task import Task, Status
import json
from os import path, listdir, remove, makedirs

class TaskManagementModule:
    id_counter: int = 0

    @staticmethod
    def loadFinalId():
        try:
            with open("finalIdValue.json", 'r') as file:
                data = json.load(file)
                TaskManagementModule.id_counter = int(data["id"])
        except FileNotFoundError:
            with open("finalIdValue.json", 'w') as file:
                json.dump({"id": str(TaskManagementModule.id_counter)}, file)
        try:
            if path.isdir("stored tasks"):
                return
            else:
                makedirs("stored tasks")
        except OSError:
            print("error\n")

    @staticmethod
    def listTasks(filter: str):
        if filter == "":
            search = listdir("stored tasks")
            for file in search:
                with open(path.join("stored tasks" ,file), 'r') as task_file:
                    data = json.load(task_file)
                    print(f"{data["description"]}\n")
        elif filter == "todo":
            search = listdir("stored tasks")
            for file in search:
                with open(path.join("stored tasks" ,file), 'r') as task_file:
                    data = json.load(task_file)
                    if data["status"] == Status.TODO:
                        print(f"{data["description"]}\n")
        elif filter == "in-progress":
            search = listdir("stored tasks")
            for file in search:
                with open(path.join("stored tasks" ,file), 'r') as task_file:
                    data = json.load(task_file)
                    if data["status"] == Status.IN_PROGRESS:
                        print(f"{data["description"]}\n")
        elif filter == "done":
            search = listdir("stored tasks")
            for file in search:
                with open(path.join("stored tasks" ,file), 'r') as task_file:
                    data = json.load(task_file)
                    if data["status"] == Status.DONE:
                        print(f"{data["description"]}\n")
        else:
            print("unkown filter parameter please us one of the following (todo, in-progress, done)\n")
            return

    @staticmethod
    def searchForFileById(id: str):
        search = listdir("stored tasks")
        for file in search:
            if id in file:
                return path.join("stored tasks", file)
        return None

    @staticmethod
    def addTask(task_description: str):
        new_task = Task(TaskManagementModule.id_counter ,task_description)
        with open(f"stored tasks/{str(TaskManagementModule.id_counter)}.json", 'w') as file:
            json.dump(new_task.to_dict(), file, indent=4)
            TaskManagementModule.id_counter += 1
        with open("finalIdValue.json", 'w') as file:
            json.dump({"id": str(TaskManagementModule.id_counter)}, file)

    @staticmethod
    def updateTask(id: str, new_description: str):
        path = TaskManagementModule.searchForFileById(id)
        if path is None:
            print("No file found\n")
            return
        with open(path, 'r') as file:
            data = json.load(file)
        data["description"] = new_description
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def deleteTask(id: str):
        search = TaskManagementModule.searchForFileById(id)
        if search is None:
            print("No file found\n")
            return
        remove(search)

    @staticmethod
    def markTask(id: str, status: str):
        search = TaskManagementModule.searchForFileById(id)
        if search is None:
            print("No file found\n")
            return
        with open(search, 'r') as file:
            data = json.load(file)
        if status == "todo":
            data["status"] = Status.TODO.value
        elif status == "in-progress":
            data["status"] = Status.IN_PROGRESS.value
        elif status == "done":
            data["status"] = Status.DONE.value
        else:
            print("unkown status please use one of the following (todo, in-progress, done).\n")
            return
        with open(search, 'w') as file:
            json.dump(data, file, indent=4)