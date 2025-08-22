# coding=windows-1251
# �����������
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
                if(priority == "�������"): 
                    print(f"����� ������")
                    return
                elif(priority == "�������"): tasksForDelay.append(name)

        if(len(tasksForDelay) > 0):
            taskNames = ""
            for s in tasksForDelay: taskNames += s + ', '
            taskNames = taskNames[0:len(taskNames) - 2]
            print(f"������� �������� ������: {taskNames}")
        else: print("������ �������")

# schedule = input()
# new_task = input()
# schedule = "������ 1 13:00 �� 14:00 �������, ������ 2 14:30 �� 15:30 �������, ������ 3 14:00 �� 15:00 �������"
schedule = "������ 12 13:00 �� 14:00 �������, ������ 13 14:30 �� 15:30 �������"
# schedule = "���������� 09:00 �� 10:00 �������, ������� �������1 12:45 �� 14:15 �������"
# schedule = "������ 20 11:00 �� 12:00 �������, ������ 21 12:30 �� 13:30 �������"
# schedule = "����������� ������ 12:10 �� 13:10 �������, ����������� 13:45 �� 15:30 �������, ���� 17:00 �� 17:45 �������"
new_task = "15:30 �� 16:30"
manager = ScheduleManager(schedule)
manager.add_task(new_task)