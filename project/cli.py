from task_mangement_module import TaskManagementModule
import re

class Cli:
    @staticmethod
    def spliter(line: str):
        value = re.findall(r'"([^"]*)"', line)
        value = " ".join(value)
        words = line.split()
        return words, value

    @staticmethod
    def executer(words : list[str], value: str):
        if words[0] == "add" and len(words) >= 2:
            TaskManagementModule.addTask(value)
        elif words[0] == "update" and len(words) == 3:
            TaskManagementModule.updateTask(words[1], words[2])
        elif words[0] == "delete" and len(words) == 2:
            TaskManagementModule.deleteTask(words[1])
        elif words[0] == "list":
            if len(words) == 2:
                TaskManagementModule.listTasks(words[1])
            elif len(words) == 1:
                TaskManagementModule.listTasks("")
        elif words[0] == "mark-in-progress" and len(words) == 2:
            TaskManagementModule.markTask(words[1], "in-progress")
        elif words[0] == "mark-todo" and len(words) == 2:
            TaskManagementModule.markTask(words[1], "todo")
        elif words[0] == "mark-done" and len(words) == 2:
            TaskManagementModule.markTask(words[1], "done")
