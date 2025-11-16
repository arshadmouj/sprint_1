# Список новых задач
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']

# Список уже завершённых задач
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1. Переносим task_005 из new_tasks в completed_tasks
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# 2. Удаляем task_007 из new_tasks (убрали из плана)
new_tasks.remove('task_007')

# 3. Выводим последнюю задачу из new_tasks (её надо взять следующей в работу)
print(new_tasks[-1])