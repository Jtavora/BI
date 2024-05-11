from controller.Controller import add_user, insert_task, get_tasks

if __name__ == '__main__':
    id_user = add_user("Joao Teste6", "teste8@teste8.com")
    insert_task("Teste", "Pendente", "Alta", "2021-12-31", id_user)

    tasks = get_tasks()
    for task in tasks:
        print(task.task)
        print(task.status)
        print(task.priority)
        print(task.deadline)
        print(task.user_id)
        print(task.created)
        print(task.updated)
        print("\n")