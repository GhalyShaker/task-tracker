from cli import Cli
from task_mangement_module import TaskManagementModule

TaskManagementModule.loadFinalId()

while True:
    line: str = input("task-cli ")
    print()
    words_of_line, value =  Cli.spliter(line)
    Cli.executer(words_of_line, value)
