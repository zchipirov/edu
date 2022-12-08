from collections import defaultdict, deque

def task_manager(tasks):
    servers_task = defaultdict(list)
    for task in tasks:
        mydeque = servers_task[task[1]]
        if len(mydeque) == 0:
            servers_task[task[1]] = deque([task[0]])
        else:
            mydeque = deque(servers_task[task[1]])
            if not task[2]:
                mydeque.append(task[0])
            else:
                mydeque.appendleft(task[0])
            servers_task[task[1]] = mydeque
    return servers_task

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))