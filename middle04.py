# coding=windows-1251
# Планировщик
import math
import re
import datetime
from datetime import datetime

class ScheduleManager:
    def __init__(self, schedule: str):
        self.schedilesList = schedule.split(", ")

    def add_task(self, task: str):
        tasksForDelay = []
        taskTimes = re.findall(r"\d{2}:\d{2}", task)
        taskStartTime = datetime.strptime(taskTimes[0], "%H:%M").time()
        taskEndTime = datetime.strptime(taskTimes[1], "%H:%M").time()

        for scheduleString in self.schedilesList:
            name = re.findall(r"^.+?\d{2}:\d{2}", scheduleString)[0]
            name = name[0:len(name) - 6]
            priority = re.findall(r"\b\w+$", scheduleString)[0]

            times = re.findall(r"\d{2}:\d{2}", scheduleString)
            startTime = datetime.strptime(times[0], "%H:%M").time()
            endTime = datetime.strptime(times[1], "%H:%M").time()

            if (taskStartTime >= startTime and taskStartTime < endTime or 
                taskEndTime > startTime and taskEndTime <= endTime or
                taskStartTime < startTime and taskEndTime > endTime):
                if(priority == "высокий"): 
                    print(f"Время занято")
                    return
                elif(priority == "обычный"): tasksForDelay.append(name)

        if(len(tasksForDelay) > 0):
            taskNames = ""
            for s in tasksForDelay: taskNames += s + ', '
            taskNames = taskNames[0:len(taskNames) - 2]
            print(f"Придётся отложить задачи: {taskNames}")
        else: print("Запись сделана")

# schedule = input()
# new_task = input()
# schedule = "Задача 1 13:00 до 14:00 обычный, Задача 2 14:30 до 15:30 обычный, Задача 3 14:00 до 15:00 высокий"
schedule = "Задача 12 13:00 до 14:00 высокий, Задача 13 14:30 до 15:30 обычный"
# schedule = "тренировка 09:00 до 10:00 обычный, деловая встреча1 12:45 до 14:15 высокий"
# schedule = "Задача 20 11:00 до 12:00 обычный, Задача 21 12:30 до 13:30 высокий"
# schedule = "контрольная работы 12:10 до 13:10 высокий, физкультура 13:45 до 15:30 обычный, ужин 17:00 до 17:45 обычный"
new_task = "15:30 до 16:30"
manager = ScheduleManager(schedule)
manager.add_task(new_task)