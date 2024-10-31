tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

from collections import defaultdict, deque

def task_manager(tasks):
    tasks_dict = defaultdict(deque)
    for i in tasks:
        if i[2] == True:
            tasks_dict[i[1]].appendleft(i[0])
        else:
            tasks_dict[i[1]].append(i[0])
    return tasks_dict
print(task_manager(tasks))
            
    